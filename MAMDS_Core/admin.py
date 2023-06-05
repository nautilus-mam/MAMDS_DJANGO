"""

    - django admin

"""
from django.contrib import admin
from .models import OperationsType, Activities, Operations


# Register your models here.
@admin.register(OperationsType)
class OperationsTypeAdmin(admin.ModelAdmin):
    list_display = ("operation_type_id", "operation_type_name", "operation_type_slug", "is_active", "create_date",
                    "last_update")


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ("activity_id", "activity_name", "mechanical_efficiency", "activity_image", "activity_slug",
                    "is_active", "create_date", "last_update")


@admin.register(Operations)
class OperationsAdmin(admin.ModelAdmin):
    list_display = ("operation_id", "operation_type_id", "activity_id", "operation_slug", "is_active", "create_date",
                    "last_update")