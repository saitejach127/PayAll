# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

# Create your views here.

def index(request):
	return render(request, 'blockchain/index.html')

def createTransaction(request):
	response = {}
	if request.method == "POST" :
		transaction = Transaction()
		transaction.fromAdd = request.POST["fromAdd"]
		transaction.toAdd = request.POST["toAdd"]
		transaction.amount = int(request.POST["amount"])
		transaction.save()

		pending = pendingTransactions()
		pending.transaction = transaction
		pending.save()
		response["success"] = True

		return render(request, 'blockchain/create.html', response)

	return render(request, 'blockchain/create.html', response)

