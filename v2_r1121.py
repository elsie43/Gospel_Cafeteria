import pandas as pd
import numpy as np
from tabulate import tabulate
df = pd.read_csv('v2.csv')
df2 = df.drop(df.columns[[0, -1]], axis = 1)

def getIndexes(dfObj, value):
    # Empty list
    listOfPos = []
     
    # isin() method will return a dataframe with boolean values, 
    # True at the positions where element exists
    result = dfObj.isin([value])
     
    # any() method will return a boolean series
    seriesObj = result.any()
 
    # Get list of column names where element exists
    columnNames = list(seriesObj[seriesObj == True].index)
    
    # Iterate over the list of columns and
    # extract the row index where element exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
 
        for row in rows:
            listOfPos.append((row, col))
             
    # This list contains a list tuples with
    # the index of element in the dataframe
    return listOfPos

choices = ["週一 09:30飯前", "週一 11:00飯前", "週一 午餐飯後", "週一 15:30飯前", "週一 17:00飯前", "週一 晚餐飯後",
"週二 09:30飯前", "週二 11:00飯前", "週二 午餐飯後", "週二 15:30飯前", "週二 17:00飯前", "週二 晚餐飯後",
"週三 09:30飯前", "週三 11:00飯前", "週三 午餐飯後", "週三 15:30飯前", "週三 17:00飯前", "週三 晚餐飯後",
"週四 09:30飯前", "週四 11:00飯前", "週四 午餐飯後", "週四 15:30飯前", "週四 17:00飯前", "週四 晚餐飯後",
"週五 09:30飯前", "週五 11:00飯前", "週五 午餐飯後", "週五 15:30飯前", "週五 17:00飯前", "週五 晚餐飯後"]

#針對飯後
#aftermeal = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

aftermeal = list(range(len(choices))) #針對全部


# set column name
colName = list(range(11)) # 0: name; 1~10: 志願
colName.append("B/S")
colName[0] = "name"

# move "弟兄/姊妹" to the end
last_column = df2.pop("弟兄/姊妹")
df2.insert(len(colName)-1, 'B/S', last_column)
df2 = df2.set_axis(colName, axis=1)

#**********************************************************#
finished_time = []
# e.g. ["週三 晚餐飯後", "週五 晚餐飯後", "週五 午餐飯後", "週四 晚餐飯後", "週三 午餐飯後", "週一 午餐飯後", ]


finished_person = []
# e.g. ["林x佳", "蔣x偉", "李x諭", "江x昇"]



#**********************************************************#
for i in range(len(finished_person)):
	df2 = df2.loc[lambda df: df["name"] != finished_person[i]]

'''
for i in range(len(aftermeal)): #印出飯後
	if choices[(aftermeal[i])] in finished_time:
		continue # for after meal
	dft = df2[(df2.isin([choices[(aftermeal[i])]])).any(axis=1)] # to get where the time section appears
	dft = dft.iloc[:,[0,-1]] # only get the name(0) and the wish(-1)
	wish = []
	listOfPositions = getIndexes(df2, choices[(aftermeal[i])])
	listOfPositions = sorted(listOfPositions,key=lambda l:l[0]) # sort the header index by the name's order
	if len(listOfPositions) > 0: # if there's person wanting this time section
		for j in range(len(listOfPositions)):
			wish.append(listOfPositions[j][1])
		dft["wish"] = wish # add a new column named "wish"
		dft = dft.sort_values(by=["wish"]) # sort the dataframe by the wish order
	print(choices[(aftermeal[i])]) # print time section name
	print(tabulate(dft, headers='keys', tablefmt='psql', showindex=False), "\n\n")

print("*********************************************************************************************")

'''




for i in range(len(choices)): #印出全部時段
	if choices[i] in finished_time:
		continue

	dft = df2[(df2.isin([choices[i]])).any(axis=1)] # to get where the time section appears
	dft = dft.iloc[:,[0,-1]] # only get the name(0) and the wish(-1)
	wish = []
	listOfPositions = getIndexes(df2, choices[i])
	listOfPositions = sorted(listOfPositions,key=lambda l:l[0]) # sort the header index by the name's order
	if len(listOfPositions) > 0: # if there's person wanting this time section
		for j in range(len(listOfPositions)):
			wish.append(listOfPositions[j][1])
		dft["wish"] = wish # add a new column named "wish"
		dft = dft.sort_values(by=["wish"]) # sort the dataframe by the wish order
	print(choices[i]) # print time section name
	print(tabulate(dft, headers='keys', tablefmt='psql', showindex=False), "\n\n")


