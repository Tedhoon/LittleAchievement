from django.urls import path
from .views import subscribe
urlpatterns = [
    
    path('subscribe/', subscribe, name="subscribe"),
    
]
