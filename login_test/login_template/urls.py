from django.urls import  path, include ,re_path
from .views import login_view ,signup_view
urlpatterns = [
    path('login/', login_view , name ="login"),
    path('' ,signup_view),
]
