from rest_framework import serializers
from .models import TelegramUsers, Mailing

class TelegramUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUsers
        fields = ('id', 'nickname', 'user_id', 'phone_number',)

class MailingSerializers(serializers.ModelSerializer):
    user = serializers.IntegerField(source = 'user.user_id')
    class Meta:
        model = Mailing
        fields = ('id', 'user', 'date', 'is_active', )

    def create(self, validated_data):
        user_registered = validated_data.pop('user').get('user_id')
        registered = TelegramUsers.objects.get(user_id=user_registered)
        user = Mailing.objects.create(user=registered)
        return user