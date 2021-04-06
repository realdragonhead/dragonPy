import csv

file_path = 'file.csv'

try:
	saved_csv_list = []
	with open(file_path, 'r' encoding='cp949') as f:
		reader = csv.reader(f, delimiter=',')
		for idx, val in enumerate(reader):
			saved_csv_list.append(val)
		f.close()
except:
	saved_csv_list = []
	with open(file_path, 'r', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=',')
		for idx, val in enumerate(reader):
			saved_csv_list.append(val)
		f.close()
