from django.urls import path
from .views import subscribe,unsubscribe
urlpatterns = [
    
    path('subscribe/', subscribe, name="subscribe"),
    path('unsubscribe/', unsubscribe, name="unsubscribe"),

]
