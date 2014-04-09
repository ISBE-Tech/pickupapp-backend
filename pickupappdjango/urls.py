from django.conf.urls import patterns, include, url
from rest_framework import routers
from pickupapp import views

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sports', views.SportViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'games', views.GameViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pickupappdjango.views.home', name='home'),
    # url(r'^pickupappdjango/', include('pickupappdjango.foo.urls')),
	
	url(r'^', include('pickupapp.urls')),
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
	
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
