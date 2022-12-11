from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (IndexPageView,
                    AboutPageView,
                    BlogPageView,
                    ContactPageView,
                    PortfolioPageView,
                    ServicesPageView,
                    TeamPageView, )

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('درباره ما/', AboutPageView.as_view(), name='about'),
    path('جشنواره رضوی/', BlogPageView.as_view(), name='blog'),
    path('ارتباط با ما/', ContactPageView.as_view(), name='contact'),
    path('ظهورمنجی/', PortfolioPageView.as_view(), name='portfolio'),
    path('پیروان عترت/', ServicesPageView.as_view(), name='services'),
    path('جوانان/', TeamPageView.as_view(), name='team'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
