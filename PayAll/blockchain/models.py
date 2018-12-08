# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Transaction(models.Model):
	fromAdd = models.CharField(max_length=100)
	toAdd = models.CharField(max_length=100)
	amount = models.IntegerField()

	def __str__(self):
		return str(self.fromAdd + " to " + self.toAdd + " of " + str(self.amount))

class pendingTransactions(models.Model):
	transaction = models.ForeignKey(Transaction, null=True, blank=True)

	def __str__(self):
		return str(self.transaction.fromAdd + "to" + self.transaction.toAdd + "of" + str(self.transaction.amount))

class Block(models.Model):
	date = models.DateField()
	index = models.IntegerField()
	_hash = models.CharField(max_length=100, blank=True)
	previousHash = models.CharField(max_length=100, blank=True)
	transactions = models.ManyToManyField(Transaction, blank=True)
	nounce = models.IntegerField()
	difficulty = models.IntegerField()

	def __str__(self):
		return str(self._hash)

