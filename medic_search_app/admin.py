from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'crated_at'
    list_display = ('user', 'role', 'birth',)
    list_display_links = ('user', 'role',)
    list_filter = ('user__is_active',)
    search_fields = ('user__username',)
    fieldsets = (
        ('Usuário', {
        'fields': ('user', 'birthday', 'image',)
        }),
        ('Função', {
        'fields': ('role',)
        }),
        ('Extras', {
        'fields': ('specialties', 'addresses',)
        }),
    )

    class Media:
        css = {
            'all': ('css/custom.css',)
        }
        js = ('js/custom.js',)

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime('%d/%m/%Y')
        
    birth.empty_value_display = '___/___/_____'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Speciality)
