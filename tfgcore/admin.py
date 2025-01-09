from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Participant


class ParticipantInline(admin.StackedInline):
    model = Participant
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ParticipantInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)