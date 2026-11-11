from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
import web.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web.urls")),
    path("berita/", views.berita, name="berita"),
    path("berita/<slug:slug>/", views.berita_detail, name="berita_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)