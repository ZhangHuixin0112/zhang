from django.urls import path
from translation.views import TranslationsView


urlpatterns = [
    path('', TranslationsView.as_view()),

]
