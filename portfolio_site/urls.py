from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home, about, contact

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Mysite Application Resr API",
        default_version="v1",
        description="Swagger docs for REST API",
        contact = openapi.Contact("Begaliyev Muhammadziyo <gmail@muhammadziyobegaliyev872.com>"),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', include('blog.urls')),  # blog ilovasi URLlari
   
    path('projects/', include('projects.urls')),  # projects ilovasi URLlari

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-docs") #docs
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)