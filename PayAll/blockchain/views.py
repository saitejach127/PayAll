# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from datetime import datetime
from hashlib import sha256

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

def blocksHome(request):
	return render(request, 'blockchain/blockHome.html')

def mineTransactions(request):
	response = {}
	if request.method == "POST" :
		block = Block()
		block.date = datetime.now()
		count = Block.objects.all().count()
		block.index = Block.objects.all()[count-1].index + 1
		block.previousHash = Block.objects.all()[count-1]._hash 

		transactions = pendingTransaction.objects.all()
		c = transactions.count()
		for i in range(c):
			block.transactions.add(transactions[i])

		string = str(block.date) + str(block.index) + str(block.previousHash) + str(block.transactions)

		block._hash = sha256(string.encode()).hexigest()
		
