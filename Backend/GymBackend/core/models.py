from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    purchase_date = models.DateField()
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    due_date = models.DateField()
    next_date = models.DateField()

    def __str__(self):
        return f"Maintenance for {self.equipment.name}"
