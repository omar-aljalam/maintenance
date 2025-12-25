from django.db import models

# Create your models here.

class MachineType(models.Model):
    name = models.CharField(max_length=50)
    maintenance_interval_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=50)
    machine_type = models.ForeignKey("MachineType", on_delete=models.CASCADE, related_name="machines")
    total_operating_hours = models.PositiveIntegerField()
    last_service_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.name
