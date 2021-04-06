import pandas as pd
import csv

 # csv 파일 리스트 변환 및 리스트 데이터 프레임 적용함수 셋

def makeDataFrameFromList(converted_csv_list):
	try:
		df = pd.DataFrame(converted_csv_list)
		header = df.iloc[0]
		df = df[1:]
		df.rename(columns = header, inplace=True)
	except Exception as e:
		# Handling error
		print(e)
		return pd.DataFrame

	return df

def makeListFromCSV(file_path):
	try:
		saved_csv_list = []
		with open(file_path, 'r', encoding='cp949') as f:
			reader = csv.reader(f, delimiter=',')
			for idx, val in enumerate(val):
				saved_csv_list.append(val)
			f.close()
	except:
		saved_csv_list = []
		with open(file_path, 'r', encoding='utf-8') as f:
			reader = csv.reader(f, delimiter=',')
			for idx, val in enumerate(val):
				saved_csv_list.append(val)
			f.close()
# resultDataFrame = MakeDataFrame(saved_csv_list)
