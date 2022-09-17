from django.contrib import admin
from django.urls import path
from  django.conf import settings
from django.conf.urls.static import static
from receitas.views import ReceitaListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/receitas/", ReceitaListView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
