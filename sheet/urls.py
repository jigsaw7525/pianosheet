from django.urls import path
from . import views

urlpatterns = [  # 設定成首頁
    path('', views.sheets, name='sheets'),
]
