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

    def get_status(self):
        hours_since_last_service = self.total_operating_hours - self.last_service_hours
        maintenance_interval = self.machine_type.maintenance_interval_hours

        if hours_since_last_service < maintenance_interval:
            return "OK"
        elif hours_since_last_service == maintenance_interval:
            return "DUE"
        else:
            return "OVERDUE"

    def hours_remaining(self):
        remaining = self.machine_type.maintenance_interval_hours - (self.total_operating_hours - self.last_service_hours)
        return remaining if remaining > 0 else 0

    def overdue_hours(self):
        overdue = self.total_operating_hours - self.last_service_hours - self.machine_type.maintenance_interval_hours
        return overdue if overdue > 0 else 0

    def increment_operating_hours(self, hours):
        if hours  <= 0:
            raise ValueError("Hours must be positive")
        self.total_operating_hours += hours
        self.save()

    def mark_serviced(self):
        self.last_service_hours = self.total_operating_hours
        self.save()
