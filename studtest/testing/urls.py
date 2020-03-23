from django.urls import path
from .views import MainTestPage, TestPage


urlpatterns = [
    path('', MainTestPage.as_view(), name='maintestpage'),
    path('<int:pk>/', TestPage.as_view(), name='testpage'),
]