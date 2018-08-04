"""fablwriter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from masal import views as masal_views
# Masal uygulamasındaki, klasöründeki views.py dosyası alınır.
from accounts import views as accounts_views
# accounts uygulamasındaki, klasöründeki views.py dosyası alınır.

# İki adet views olup birbirine karışmasın diye as ibaresi ile farklı isimler verilir.
urlpatterns = [
    path('', masal_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('fabl/create', masal_views.fabl_create, name='create'),
    # Masal uygulamasındaki views içinde tanımlanan fabl_create kullan. isim olarak da create ver.
    path('fabl/publish/<int:id>/', masal_views.fabl_publish, name='publish'),
    # Diğerinden farklı olarak int:id ile id numarasına göre otomatik url yazılır.
    path('accounts/',include('django.contrib.auth.urls')),
    # Buradaki include amacı django auth içinde varsayılan views leri getirir.
    path('about/', accounts_views.about, name='about'),
    path('registration/login/', accounts_views.login, name='login'),
    # accounts uygulamasındaki views içinde tanımlanan login sınıfını kullan. isim olarak da login ver.
    path('accounts/profile/', accounts_views.profile, name='profile'),
    path('registration/signup/', accounts_views.signup, name='signup'),
]
