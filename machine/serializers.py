from rest_framework import serializers

from .models import Machine, MachineType

class MachineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineType
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    remaining = serializers.SerializerMethodField()
    overdue = serializers.SerializerMethodField()
    machine_type = serializers.PrimaryKeyRelatedField(queryset=MachineType.objects.all())

    def get_status(self, obj):
        return obj.get_status()

    def get_remaining(self, obj):
        return obj.hours_remaining()

    def get_overdue(self, obj):
        return obj.overdue_hours()

    class Meta:
        model = Machine
        fields = [
            "name",
            "machine_type",
            "total_operating_hours",
            "last_service_hours",
            "status",
            "remaining",
            "overdue",
        ]
