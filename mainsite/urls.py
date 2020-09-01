from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('blog', include('blog.urls')),
    path('about', include('about.urls')),
    path('contact', include('contact.urls')),
    path('details', include('details.urls')),
    path('pricing', include('pricing.urls')),
    path('service', include('service.urls')),



]

# this section for media file

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)