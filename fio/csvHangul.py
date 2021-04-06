import csv

def csvHelp():
	print('makeCSVtoList(file_path) return List')
	print('makeListtoCSV(file_path, target_list)')
	print('appendListtoCSV(file_path, target_list)')

# CSV -> List
def makeCSVtoList(file_path):
	try:
		saved_csv_list = []
		with open(file_path, 'r' encoding='cp949') as f:
			reader = csv.reader(f, delimiter=',')
			for idx, val in enumerate(reader):
				saved_csv_list.append(val)
			f.close()
	except Exception as e:
		saved_csv_list = []
		with open(file_path, 'r', encoding='utf-8') as f:
			reader = csv.reader(f, delimiter=',')
			for idx, val in enumerate(reader):
				saved_csv_list.append(val)
			f.close()
	return saved_csv_list

# List -> CSV
def makeListtoCSV(file_path, target_list):
	try:
		narray = np.array(target_list)
		np.savetxt(file_path, ndarray, delimiter=',')	
	except Exception as e:
		print('Error : makeListtoCSV(file_path, target_list)')
		print(e)

# Append List to exist CSV file
def appendListtoCSV(file_path, target_list):
	try:
		with open(file_path, 'a', newline='') as f:
			c_writer = csv.writer(f)
			c_writer.writerow(target_list)
			f.close()
	except Exception as e:
		print('Error : appendListtoCSV(target_file_path, LIST)')
		print(e)
			
