from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import index,contact_view,register_view

from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("",index,name="index"),
    path("contact/",contact_view,name="contact_view"),
    path("register/",register_view,name="register_view"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("login/",auth_views.LoginView.as_view(template_name ="core/login.html",authentication_form = LoginForm),name="login_view")
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
