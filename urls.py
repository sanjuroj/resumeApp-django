from django.conf.urls import url, include
from rest_framework import routers
from .views import APIAll
from django.views.generic import TemplateView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'^$', APIAll, 'api_all')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', APIAll.as_view(), name='api_all'),
    url(r'^', TemplateView.as_view(template_name='resume/resume.html'))
    # url(r'^api/', include(router.urls))
]
