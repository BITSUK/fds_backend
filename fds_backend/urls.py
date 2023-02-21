
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path('fds/', include('restapp.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='admin/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)