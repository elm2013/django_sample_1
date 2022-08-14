from django.conf.urls import url
from django.conf.urls.static import static

from templetProject import settings
from . import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index'),
    url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^article/(?P<id>\d+)/$', views.SinglePage.as_view(), name='article'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static('contact/static/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('about/static/', document_root=settings.STATIC_ROOT)
    # urlpatterns += static('article/<>/static/', document_root=settings.STATIC_ROOT)