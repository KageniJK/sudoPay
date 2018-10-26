from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^sudopay/$' , views.pay_index , name='pay_index') ,
    url(r'^member/(?P<user_username>\w+)/$', views.profile, name='userprofile'),
    url(r'^account/edit$', views.update_profile, name='edit_profile'),
    url(r'^sudopay/checkout/(\d+)$' , views.check_out , name ='check_out') ,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
