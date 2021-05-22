def over_price(filename):
	items={}
	with open(filename) as f:
		for line in f:
			total=over = 0
			name,date,cost = line.strip().split()
			total =1
			if float(cost[1:]) > 4.00:
				over=1
			if name not in items:
				items[name] = [total,over]
			else:
				items[name][0] +=total
				items[name][1] +=over
	for item in items:
		print(f'{item}: {float(items[item][1]/items[item][0]*100):.1f}%')

over_price('content.txt')
