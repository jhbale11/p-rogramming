from django.contrib import admin
from blog.models import Protest
from blog.models import User
from blog.models import Participation
# Register your models here.


class ProtestAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

class UserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'email']
    list_display_links = ['nickname']

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['protest', 'user']
    list_display_links = ['protest']

#class TypeAdmin(admin, ModelAdmin):
#    list_display = ['TYPE_CHOICES']
#    list_display_links = ['TYPE_CHOICES']



admin.site.register(Protest,ProtestAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Participation,ParticipationAdmin)
#admin.site.register(Type,TypeAdmin)
