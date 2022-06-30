from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Task, Position, Categories, Unit, Material, Service, Object


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = []

    model = CustomUser
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm

    list_display = [ 'name', 'position',  'email']
    list_filter = ('position',)

    # Add user
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Данные сотрудника',
            {
                'fields': (
                    'name',
                    'phone',
                    'description',
                    'position',
                    'isWorker'
                )
            }
        )
    )

    # Edit user
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Данные сотрудника',
            {
                'fields': (
                    'name',
                    'phone',
                    'description',
                    'position',
                    'isWorker'
                )
            }
        )
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'material')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('service','size','date_start', 'date_finish', 'material_status','completeness', 'worker_id')
    list_filter = ('object','category')
    search_fields = ('service',)


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name','location','client_name', 'worker_id')
    search_fields = ('name','location', 'worker_id__name')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name','price','expenditure')
    search_fields = ('name', )


admin.site.register(Unit)
admin.site.register(Categories)

