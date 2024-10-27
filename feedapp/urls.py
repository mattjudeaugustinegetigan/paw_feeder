from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('signup/', views.signup, name='signup'),  # Signup page
    path('profile/', views.profile, name='profile'),  # User profile page
    path('add_pet/', views.add_pet, name='add_pet'),  # Add pet page
    path('add_dogorcat/', views.add_dogorcat, name='add_dogorcat'),  # Add dog or cat page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files in debug mode
