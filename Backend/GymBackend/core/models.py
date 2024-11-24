from django.db import models
import datetime

# Function to generate custom Admin ID with role
def generate_admin_id(instance):
    year = datetime.datetime.now().year
    role = instance.role.upper()[:2] if instance.role else "MG"  # Use only the first two characters of the role
    count = Admin.objects.filter(admin_id__startswith=f"{year}{role}").count() + 1
    return f"{year}{role}{str(count).zfill(4)}"  # Total length will be 10 characters (Year(4) + Role(2) + Count(4))

def generate_equipment_id(instance):
    year = datetime.datetime.now().year
    equipment_type = instance.name.upper()[:3] if instance.name else "GEN"  # Default to "GEN" if name is not provided
    count = Equipment.objects.filter(equipment_id__startswith=f"{equipment_type}{year}").count() + 1
    return f"{equipment_type}{year}{str(count).zfill(3)}"  # Total length will be 10 characters (EquipmentType(3) + Year(4) + Count(3))

def generate_maintenance_id(equipment_id):
    equipment_type = equipment_id[:3]  # Extract equipment type (first 3 characters)
    due_date = datetime.datetime.now().strftime("%Y%m")  # Format as YYYYMM
    count = Maintenance.objects.filter(maintenance_id__startswith=f"{equipment_type}{due_date}").count() + 1
    return f"{equipment_type}{due_date}{str(count).zfill(3)}"  # Total length will be 12 characters (EquipmentType(3) + DueDate(6) + Count(3))

class Admin(models.Model):
    admin_id = models.CharField(max_length=10, primary_key=True, blank=True)  # Fixed length 10
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    role = models.CharField(max_length=50, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.admin_id:
            self.admin_id = generate_admin_id(self)  # Generate admin_id based on role
        super(Admin, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    equipment_id = models.CharField(max_length=10, primary_key=True, blank=True)  # Fixed length 10
    name = models.CharField(max_length=255)
    purchase_date = models.DateField()
    condition = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.equipment_id:
            self.equipment_id = generate_equipment_id(self)  # Generate equipment_id when it's not provided
        super(Equipment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Maintenance(models.Model):
    maintenance_id = models.CharField(max_length=12, primary_key=True, blank=True)  # Fixed length 12
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    due_date = models.DateField()
    next_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.maintenance_id:
            # Generate maintenance_id based on equipment_id after saving the equipment
            self.maintenance_id = generate_maintenance_id(self.equipment.equipment_id)  
        super(Maintenance, self).save(*args, **kwargs)

    def __str__(self):
        return f"Maintenance for {self.equipment.name}"
