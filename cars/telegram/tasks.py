import requests
from celery import shared_task
from .models import TelegramUsers, Mailing

@shared_task
def telegram_mailing():
    users = Mailing.objects.filter(is_active=True)
    for user1 in users:
        bot_url = 'https://api.telegram.org/bot5964508466:AAFxTaOo61l-M6J0TUuDX9SxSCXcKdpMqA0/sendMessage'
        message = 'Рассылка, которая работает каждые 30 секунд'
        data = {
            'chat_id': user1.user,
            'text': message,
        }
        response = requests.post(bot_url, data)
        if response.status_code == 201:
            user1.save()