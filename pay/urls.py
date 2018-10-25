from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^/shop' , views.pay_index , name='pay_index') ,
    url(r'^member/(?P<user_username>\w+)/$', views.profile, name='userprofile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
