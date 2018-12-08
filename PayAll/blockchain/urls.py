from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^Transact/', createTransaction),
	url(r'^$', blocksHome),
	url(r'^mineTransact/', mineTransactions),
	url(r'^check/', checkChain),
]
