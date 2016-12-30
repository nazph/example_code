from collections import defaultdict, Counter

def return_values(list_of_dict):
	results = defaultdict(int)
	for data in list_of_dict:
		results[data['symbol']] += int(data['qty'])

	print results
	for symbol, total in results.iteritems():
		print('{} - {}'.format(symbol, total))


list_of_dict = [{"id":"110235","symbol":"ccl","qty":900,"available":3,"time":"2016-05-05T08:00:00.169646Z"},
                {"id":"110246","symbol":"ccl","qty":550,"available":16,"time":"2016-05-05T08:01:05.167356Z"},
                {"id":"110745","symbol":"ssi","qty":1550,"available":24,"time":"2016-05-05T08:01:07.173386Z"},
   {"id":"110268","symbol":"tcl","qty":270,"available":21,"time":"2016-05-05T08:01:15.089586Z"},
   {"id":"110294","symbol":"ccl","qty":690,"available":57,"time":"2016-05-05T08:01:24.236786Z"},
   {"id":"110268","symbol":"tcl","qty":740,"available":38,"time":"2016-05-05T08:01:28.145786Z"}]

def sum_symbols(data):
	symbols = {}
	for a in data:
		if a['symbol'] in symbols:
			symbols['qty'] += int(a['available'])
			symbols['id'] = a['id']
			symbols[a['symbol']] = a['symbol']
			symbols['time'] = a['time']
		else:
			symbols['qty'] = int(a["available"])
			symbols['id'] = a['id']
			symbols[a['symbol']] = a['symbol']
			symbols['time'] = a['time']

		print symbols


	print symbols

def reduce_list(list_of_dict):
	r_list = defaultdict(Counter)
	for data in list_of_dict:
		counts = Counter({k:v for k,v in data.items() if k not in ('id', 'symbol', 'time')})
		r_list[data['symbol']] +=counts



	print r_list
	print type(r_list)


def re_list(list_of_dict):
	results = {}
	for i in list_of_dict:
		if i['symbol'] not in results:
			results[i['symbol']] = {'id':i['id'],'symbol':i['symbol'],'qty':0, 'available':0, 'time': i['time']}
		results[i['symbol']]['qty'] +=i['qty']
		results[i['symbol']]['available'] += i['available']

	print results.values()



re_list(list_of_dict)





reduce_list(list_of_dict)






