from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, LoginView


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

]
