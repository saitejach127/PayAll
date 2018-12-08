# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
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
		block.difficulty = int(request.POST["difficulty"])
		block.nounce = 1
		string = str(block.date) + str(block.index) + str(block.previousHash) + str(block.nounce)

		block._hash = sha256(string.encode()).hexdigest()
		block.save()
		block = Block.objects.get(index=block.index)

		transactions = pendingTransactions.objects.all()

		c = transactions.count()
		for i in range(c):
			block.transactions.add(transactions[i].transaction)
		pendingTransactions.objects.all().delete()
		string = str(block.date) + str(block.index) + str(block.previousHash) + str(block.transactions) + str(block.nounce)

		block._hash = sha256(string.encode()).hexdigest()

		curr_hash = block._hash

		while True:
			if curr_hash[:block.difficulty] == "0"*block.difficulty :
				block._hash = curr_hash
				break
			block.nounce += 1
			s = str(block.date) + str(block.index) + str(block.previousHash) + str(block.transactions) + str(block.nounce)
			curr_hash = sha256(s.encode()).hexdigest()

		block.save()
		response["hash"] = block._hash
		return render(request, "blockchain/mine.html", response)

	return render(request, "blockchain/mine.html", response)

def checkChain(request):
	blocks = Block.objects.all()
	count = Block.objects.all().count()
	for i in range(count-1):
		if(blocks[i]._hash != blocks[i+1].previousHash):
			print("not working")
			return render(request, "blockchain/check.html")
	return redirect("/")

