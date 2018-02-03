from django.conf.urls import url
from django.contrib import admin

from pbs import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^start/$', views.start , name='start'),
    url(r'^patient_registration/$', views.patient_registration , name='patient_registration'),
    url(r'^bill_details/$', views.bill_details , name='bill_details'),
    url(r'^treatments_needed/$', views.treatments_needed , name='treatments_needed'),
    url(r'^general/$', views.general , name='general'),
    url(r'^admin/', admin.site.urls),
]
