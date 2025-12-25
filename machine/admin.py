from django.contrib import admin

from .models import Machine, MachineType

# Register your models here.

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "machine_type",
        "total_operating_hours",
        "last_service_hours",
        "status",
        "hours_remaining",
        "overdue_hours",
    )

    def status(self, obj):
        return obj.get_status()

    list_filter = (
        "machine_type",
    )

@admin.register(MachineType)
class MachineTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "maintenance_interval_hours",
    )