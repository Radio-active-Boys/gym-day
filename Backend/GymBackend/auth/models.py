from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from core.models import Admin  # Assuming you have these models in the core app
from workout.models import Trainer  # Assuming you have these models in the workout app
from membership.models import Member  # Assuming you have these models in the membership app


class UserAuth(models.Model):
    # This will store the user information for authentication.
    USER_ROLES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('trainer', 'Trainer'),
    )

    user_id = models.IntegerField()  # The primary key ID of the user (can be Admin, Trainer, or Member)
    role = models.CharField(max_length=20, choices=USER_ROLES)  # User's role
    hashed_password = models.CharField(max_length=255)  # Hashed password

    def set_password(self, password):
        """Sets the password by hashing it."""
        self.hashed_password = make_password(password)

    def check_password(self, password):
        """Checks the given password with the stored hash."""
        return check_password(password, self.hashed_password)

    def save(self, *args, **kwargs):
        """Override the save method to check for role and user_id existence."""
        # Check if the provided user_id exists in the corresponding role table
        if self.role == 'admin':
            if not Admin.objects.filter(id=self.user_id).exists():
                raise ValueError("Admin ID does not exist.")
        elif self.role == 'member':
            if not Member.objects.filter(id=self.user_id).exists():
                raise ValueError("Member ID does not exist.")
        elif self.role == 'trainer':
            if not Trainer.objects.filter(id=self.user_id).exists():
                raise ValueError("Trainer ID does not exist.")
        else:
            raise ValueError("Invalid role.")

        super(UserAuth, self).save(*args, **kwargs)  # Call the parent class's save method


# Create a class for the User Registration
class UserRegistration(models.Model):
    user_id = models.IntegerField()
    role = models.CharField(max_length=20, choices=UserAuth.USER_ROLES)
    password = models.CharField(max_length=255)

    def save_user(self):
        """Create the user in the auth table after setting password"""
        user_auth = UserAuth(user_id=self.user_id, role=self.role)
        user_auth.set_password(self.password)
        user_auth.save()

    @staticmethod
    def check_user_exists(user_id, role):
        """Check if the user exists in the role-specific table."""
        if role == 'admin':
            return Admin.objects.filter(id=user_id).exists()
        elif role == 'member':
            return Member.objects.filter(id=user_id).exists()
        elif role == 'trainer':
            return Trainer.objects.filter(id=user_id).exists()
        return False


# Create class for password reset logic
class PasswordResetRequest(models.Model):
    user_id = models.IntegerField()
    role = models.CharField(max_length=20, choices=UserAuth.USER_ROLES)
    new_password = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def reset_password(self):
        """Reset password if the user exists and match role."""
        if UserRegistration.check_user_exists(self.user_id, self.role):
            user_auth = UserAuth.objects.get(user_id=self.user_id, role=self.role)
            user_auth.set_password(self.new_password)
            user_auth.save()
        else:
            raise ValueError("User does not exist or role mismatch.")
