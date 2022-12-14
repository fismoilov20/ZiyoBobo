"""ZiyoBobo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),

    path('yangiliklar', YangiliklarView.as_view()),
    path('yangiliklar/<int:pk>', NewsView.as_view()),

    path('mehnat', MehnatView.as_view()),
    path('qabul', QabulView.as_view()),
    path('biz-haqimizda', BizHaqimizdaView.as_view()),
    path('foydalanish-shartlari', FoydalanishView.as_view()),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>/", set_language, name="set-language"),
]