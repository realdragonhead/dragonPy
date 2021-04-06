import csv

try:
	with open('file.txt', 'r') as f:
		reader = csv.reader(f)
		data_loc = next(reader)
		data_loc = data_loc[0]
		f.close()
except:
	with open('file.txt', 'w+') as f:
		f.write('content')
		f.close()
