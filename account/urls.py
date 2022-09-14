from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import RegisterUserView, LoginUserView

urlpatterns = [
    path('registration/', RegisterUserView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='authentication'),
    # path('social-auth/', include('social_django.urls', namespace="social")),
    path('logout/', LogoutView.as_view(), name='logout'),
]
