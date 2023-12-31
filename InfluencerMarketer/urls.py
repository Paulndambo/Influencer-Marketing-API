from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Influencer Marketing API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)


def home(request):
   return render(request, "ads.html")

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path("payments/", include("apps.payments.urls")),
    path("users/", include("apps.users.urls")),
    path("products/", include("apps.products.urls")),
    path("analytics/", include("apps.analytics.urls")),
    path("reports/", include("apps.reports.urls")),
    path("integrations/", include("apps.integrations.urls")),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)