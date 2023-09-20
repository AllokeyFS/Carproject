from django.db import models

class TelegramUsers(models.Model):
    nickname = models.CharField(max_length=30, verbose_name='Nickname')
    user_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True)
    phone_number = models.CharField(max_length=50, verbose_name='Phone number')


    def __str__(self) -> str:
        return f'{self.nickname} {self.phone_number}'
    

    class Meta:
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'


class Mailing(models.Model):
    user = models.ForeignKey(TelegramUsers, on_delete=models.CASCADE, verbose_name='User')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Registration date')
    is_active = models.BooleanField(default=True, verbose_name='Subscribed')

    def __str__(self) -> str:
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        unique_together = ('user',)