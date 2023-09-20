from django.contrib import admin
from .models import TelegramUsers, Mailing

@admin.register(TelegramUsers)
class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'user_id', 'phone_number',)

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'is_active', )
    