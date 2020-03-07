# To Check whether all cv values are 0 or not.
def check(cv):
	for x in cv:
		if x == 0:
			t=False
		else:
			t=True
			break
	return t
# To calculate the profit of the stocks.
def stock_invest(saving,cv,fv):
	# To calculate profit of stocks.
	profit=[fv[x]-cv[x] for x in range(len(cv))]
	print(profit)
	stocks=[]
	# Copy the cv.
	cv1=cv.copy()
	# Continue the loop to check whether cv1 value is 0.
	while check(cv1):
		# To check profit is >= 0
		if profit[cv1.index(max(cv1))]>=0:
			# To check if saving is not equal.
			if saving!=max(cv1):
				stocks.append(max(cv1))
				cv1[cv1.index(max(cv1))]=0
				print(cv1)
			# assign 0 if saving ==max(cv1)
			else:
				cv1[cv1.index(max(cv1))]=0
				print(cv1)
		# if profit<0.
		else:
			cv1[cv1.index(max(cv1))]=0
			print(cv1)
	max_profit=0
	print(stocks)
	# To calculate the max profit.
	for x in stocks:
		max_profit+=fv[cv.index(x)]-cv[cv.index(x)]
	print(max_profit)
# Declartion of saving , currentvalue, future value
saving=40
currentValue = [23, 19, 40, 17, 10]
futureValue  = [22, 18, 40, 17, 9]
stock_invest(saving,currentValue,futureValue)
