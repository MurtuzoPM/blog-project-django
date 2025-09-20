from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),   # блог
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('signup/', blog_views.signup, name='signup'),       # регистрация
    
]
