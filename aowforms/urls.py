from django.urls import path
from aowforms.views import home


urlpatterns = [
    path('', home, name="home")
]
