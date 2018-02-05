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
    url(r'^icu/$', views.icu , name='icu'),
    url(r'^transfers/$', views.transfers , name='transfers'),
    url(r'^bill_generator/$', views.bill_generator , name='bill_generator'),
    url(r'^all_patient_details/$', views.all_patient_details , name='all_patient_details'),
    url(r'^admin/', admin.site.urls),
]
