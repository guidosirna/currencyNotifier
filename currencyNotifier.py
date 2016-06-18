#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import smtplib
import datetime

initialSavings = float(1)

def setCurrencyFrom():
	currencyFrom = raw_input("Specify origin Currency: ")
	while isinstance(currencyFrom,str) and currencyFrom.isalpha() == True and len(currencyFrom) == 3:
		return currencyFrom
	else:
		print('Type a valid ISO 4217 Currency Code. Help: http://www.xe.com/iso4217.php')
		return setCurrencyFrom()

def setCurrencyTo():
	currencyTo = raw_input("Specify destiny Currency: ")
	while isinstance(currencyTo,str) and currencyTo.isalpha() == True and len(currencyTo) == 3:
		return currencyTo
	else:
		print('Type a valid ISO 4217 Currency Code. Help: http://www.xe.com/iso4217.php')
		return setCurrencyTo()

def setAmount():
	amount = float(raw_input("Specify an amount: "))
	if isinstance(amount,float):
		amount = '{0:.2f}'.format(amount)
		return float(amount)
	else:
		print('Amount must be a number.')
		setAmount()

def setCapValue():
	capValue = float(raw_input("Set a Cap value: "))
	if isinstance(capValue,float):
		return capValue
	else:
		print('Cap value must be a number.')
		setCapValue()

def getExchangeValue(currencyFrom,currencyTo):
	link = "https://www.google.com/finance/converter?a=$1&from="+currencyFrom+"&to="+currencyTo
	url = urllib2.urlopen(link)
	content = url.read()
	soup = BeautifulSoup(content, 'html.parser')
	exchangeValue = soup.span.get_text()
	exchangeValue = exchangeValue.replace(' ', '')[:-5].upper()
	return float(exchangeValue)

def getExchangeRate(exchangeValue,capValue):
	exchangeRate = "{0:.2f}%".format((1 - exchangeValue / capValue)*-100)
	return exchangeRate

def result(exchangeValue,capValue,amount):
	print 
	if exchangeValue > capValue:
		return(" "+str(datetime.datetime.now())+"\n Exchange value is "+str(getExchangeRate(exchangeValue,capValue))+" greater than Cap. \n Exchange value: "+str(exchangeValue)+" "+currencyTo+". \n Balance: "+str("{0:.2f}".format((amount*exchangeValue)+(amount*exchangeValue)-(initialSavings*capValue)))+" "+currencyTo+". \n Earnings: "+str("{0:.2f}".format((amount*exchangeValue)-(initialSavings*capValue)))+" "+currencyTo+".  \n Sell now!\n")
		pass
	else:
		if exchangeValue < capValue:
			return(" "+str(datetime.datetime.now())+"\n Exchange value is not greater than Cap yet. \n Exchange value: "+str(exchangeValue)+" "+currencyTo+". \n Balance: "+str("{0:.2f}".format(amount*exchangeValue))+" "+currencyTo+". \n Don\'t sell yet.\n")
			pass
		else:
			if exchangeValue == capValue:
				return(" "+str(datetime.datetime.now())+"\n Exchange value is equal than Cap. \n Exchange value: "+str(exchangeValue)+" "+currencyTo+". \n Balance: "+str(amount*exchangeValue)+" "+currencyTo+".\n")
				pass

print result(getExchangeValue(setCurrencyFrom(),setCurrencyTo()),setCapValue(),initialSavings)