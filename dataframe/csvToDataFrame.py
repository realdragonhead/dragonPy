import pandas as pd
import csv

# Convert list to dataframe
def makeListtoDataFrame(converted_csv_list, header):
	try:
		df = pd.DataFrame(converted_csv_list)
		if header == True:
			columns_header = df.iloc[0]
			df = df[1:]
			df.rename(columns = columns_header, inplace=True)
	except Exception as e:
		# Handling error
		print(e)
		return pd.DataFrame
	return df

def makeDataFrametoList(target_dataframe, header, header_split):
	try:
		if header == True:
			if header_split == True:
				return columns_header, result_list
			else:
				return result_list
		else:
			return result_list
	except Exception as e:
		print(e)

def makeCSVtoDataFrame(file_path, header)
	# Open CSV file
	try:
		try:
			saved_csv_list = []
			with open(file_path, 'r', encoding='cp949') as f:
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
	except Exception as e:
		print(e)
		return

	# Make DataFrame
	try:
		df = pd.DataFrame(saved_csv_list)
		if header == True:
			column_header = df.iloc[0]
			df = df[1:]
			df.rename(columns = column_header, inplace=True)
	except Exception as e:
		print(e)
		return

	return df
			
