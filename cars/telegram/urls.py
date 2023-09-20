from django.urls import path
from . import views

urlpatterns = [
    path('telegramuser/', views.TelegramUsersVeiwSets.as_view(
        {
            'get':'list',
            'post':'create',
        }
    )),
    path('telegramuser/<int:pk>/',views.TelegramUsersVeiwSets.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),
    path('mailing/', views.TrueMailingViewSets.as_view(
        {
            'get':'list',
            'post':'create',
        }
    )),
    path('mailing/<int:pk>/',views.TrueMailingViewSets.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),
    path('mailingfalse/', views.FalseMailingViewSets.as_view(
        {
            'get':'list',
            'post':'create',
        }
    )),
    path('mailingfalse/<int:pk>/',views.FalseMailingViewSets.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),
]