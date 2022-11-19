import datetime

import pandas as pd
import time as t

df=pd.read_excel('./data.xlsx',sheet_name='Sheet1')
# print(df)
# #append the df
# def replace_df():
#     df = pd.read_excel('./data.xlsx', sheet_name='Sheet1')
#     find_name = df[df['Name'] == str(input("Type the old person\'s name here:  ")).upper()].index[0]
#     print(df.loc[find_name])
#     new_name=str(input('Type the new person\'s name here: ')).upper()
#     new_number=int(input('Type the new person\'s phone numbere here: '))
#     df=df.replace((df.loc[find_name][1]),new_name)
#     df=df.replace((df.loc[find_name][2]),new_number)
#     df.to_excel('data.xlsx',index=False)
#     df=pd.read_excel('./data.xlsx',sheet_name='Sheet1')
#     print(df)
# # print(df[find_name][1],df[find_name][2])
# replace_df()
a={'room number':[],'name':[], 'phone':[],'date':[]}
today = datetime.date.today()
dt = today + datetime.timedelta(days=-today.weekday(), weeks=0)
for i in range(0,2):
    for j in range(len(df['Room Number'])):
        a['room number'].append(df['Room Number'][j])
        dt=dt+datetime.timedelta(days=7)
        a['date'].append(dt)
        a['name'].append(df['Name'][j])
        a['phone'].append(df['Phone'][j])
    # t.sleep(2)
# print(a)
maindf=pd.DataFrame(a)
# maindf.to_excel('./data.xlsx',sheet_name='Sheet2')
# print(maindf)
#----------------creates new exel sheet with the old df and time in another sheets----------------------
# with pd.ExcelWriter('output.xlsx') as writer:
#     df.to_excel(writer,sheet_name='sheet 1')#sheet_name=sheet1)
#     maindf.to_excel(writer, sheet_name='sheet 2')#,sheet_name=sheet2)





import pandas as pd
import datetime

class schuyler:
    def __init__(self):
        pass
    def dataframe(): #reads the df from the index and creates a new master data for time(turn)
        index_df=pd.read_excel('./data.xlsx',sheet_name='Sheet1')
        today = datetime.date.today()
        dt = today + datetime.timedelta(days=-today.weekday(), weeks=0)
        # index_df['Turn']=
        a = {'room number': [], 'name': [], 'phone': [], 'date': []}
        for i in range(0, 200):
            for j in range(len(index_df['Room Number'])):
                dt = dt + datetime.timedelta(days=7)
                a['room number'].append(index_df['Room Number'][j])
                a['date'].append(dt)
                a['name'].append(index_df['Name'][j])
                a['phone'].append(index_df['Phone'][j])
        aa = pd.DataFrame(a)
        with pd.ExcelWriter('./output.xlsx') as writer:
            index_df.to_excel(writer,sheet_name='indexDF')
            aa.to_excel(writer,sheet_name='aa')

a=schuyler.dataframe()


