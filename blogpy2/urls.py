"""blogpy2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # define default or index page that declared in urls.py of blog application
    url(r'^', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('contact/static/', document_root=settings.STATIC_ROOT)

    '''
    http://127.0.0.1:8000/about44/static22/css/vendor.css
    وقتی یو آر ال بالا زده میشود می آید و خط زیر را بررسی میکند و میفهمد که وقتی about44/static22 زده شد
    باید برود و پوشه ی document_root را برگرداند
    توجه شود که اگر مقدار document_root =settings.STATIC_ROOT باشد می رود و 
    پوشه staticfiles را بر میگرداند. در واقع در این حالت نیاز است که حتما collectstatic انجام شده باشد
    دقت شود که در فایل html هم باید مقدار static22 نوشته شود تا یو آر ال بالا به درستی ساخته شود
    و بعد از ساخته شدن یو آر ال، خط زیر به درستی کار کند 
    '''
    urlpatterns += static('about44/static22/', document_root='static')
