from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^sign',views.signup,name='signup'),
    url(r'^$', views.index, name='index'),
    url(r'^add/(\d+)/',views.add_to_cart,name='add'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^remove/(\d+)',views.delete_cart,name='delete'),
    url(r'^empty',views.empty,name='empty'),
    url(r'^image',views.image,name='image'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
