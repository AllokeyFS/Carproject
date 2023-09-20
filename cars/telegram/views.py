import django_filters
from django.shortcuts import render
from rest_framework import filters, viewsets
from .models import TelegramUsers, Mailing
from .serializers import TelegramUsersSerializer, MailingSerializers

class TelegramUsersVeiwSets(viewsets.ModelViewSet):
    queryset = TelegramUsers.objects.all()
    serializer_class = TelegramUsersSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_fields = ('user_id', )

class TrueMailingViewSets(viewsets.ModelViewSet):
    queryset = Mailing.objects.filter(is_active=True)
    serializer_class = MailingSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_fields = ('user__user_id', )

class FalseMailingViewSets(viewsets.ModelViewSet):
    queryset = Mailing.objects.filter(is_active=False)
    serializer_class = MailingSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_fields = ('user__user_id', )