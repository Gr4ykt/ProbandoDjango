from django.contrib import admin
from .models import empleado, habilidades

# Register your models here.
admin.site.register(habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display =(
        'name',
        'short_name',
        'job',
        'Departamento',
        'full_name',
    )
    #
    def full_name(self, obj):
        print(obj)
        return obj.name + " " + obj.short_name
    #
    search_fields = ('name',)
    list_filter = ('job', 'habilidad')
    filter_horizontal = ('habilidad',)

admin.site.register(empleado, EmpleadoAdmin)