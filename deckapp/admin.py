
from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")



class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "description","created_at")



admin.site.register(User, UserAdmin)
admin.site.register(Deck, GroupAdmin)
admin.site.register(Message)
admin.site.register(SecurityKeys)


