from django.urls import path
from translation.views import translationsView


urlpatterns = [
    path('', translationsView, name='translationsView'),

]
