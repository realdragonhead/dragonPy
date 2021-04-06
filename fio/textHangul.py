import csv

# One line reader
def oneLineTextReader(file_path):
	data = ''
	try:
		with open(file_path, 'r', encoding='cp949') as f:
			reader = csv.reader(f)
			data = next(reader)
			f.close()
	except:
		with open(file_path, 'r', encoding='utf-8') as f:
			reader = csv.reader(f)
			data = next(reader)
			f.close()
	return data
