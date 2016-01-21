from django.contrib import admin
from protest.models import Protest
from protest.models import User
from protest.models import Participation
# Register your models here.


class ProtestAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

class UserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'email']
    list_display_links = ['nickname']

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['protest_name', 'user_id']
    list_display_links = ['protest_name']

admin.site.register(Protest,ProtestAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Participation,ParticipationAdmin)
