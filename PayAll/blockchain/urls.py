from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^Transact/', createTransaction),
	url(r'^$', blocksHome),
]
