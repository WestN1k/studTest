from django.urls import path
from .views import MainTestPage, TestPage, Result


urlpatterns = [
    path('', MainTestPage.as_view(), name='maintestpage'),
    path('<int:pk>', TestPage.as_view(), name='testpage'),
    path('<int:pk>/results', Result.as_view(), name='resultspage')
]