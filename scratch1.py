
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import datetime
from datetime import date

class schuyler:
    def __init__(self):
        pass
    def dataframe(self): #reads the df from the index and creates a new master data for time(turn)
        index_df=pd.read_excel('./data.xlsx',sheet_name='Sheet1',usecols=['Room Number','Name','Phone'])
        today = date(2022,12,26)
        dt = today + datetime.timedelta(days=-today.weekday(), weeks=0)
        a = {'room number': [], 'name': [], 'phone': [], 'date': []}
        for i in range(0, 200):
            for j in range(len(index_df['Room Number'])):
                dt = dt + datetime.timedelta(days=7)
                a['room number'].append(index_df['Room Number'][j])
                a['date'].append(dt)
                a['name'].append(index_df['Name'][j])
                a['phone'].append(index_df['Phone'][j])
        aa = pd.DataFrame(a)
        with pd.ExcelWriter('./data.xlsx') as writer:
            index_df.to_excel(writer,sheet_name='Sheet1')
            aa.to_excel(writer,sheet_name='finalSchedule')

    def old_name(self): #a function to check the input and the existing list of names
        main_df = pd.read_excel('./data.xlsx', sheet_name='Sheet1', usecols=['Room Number', 'Name', 'Phone'])
        df = main_df
        temp_list=df['Name'].to_list() #convert the names toa list to match the input
        _condition = True
        while _condition:
            en_ = str(input("Type the old person\'s name again:  ")).upper()
            if en_ in temp_list:
                existing_name = en_
                _condition = False
                return existing_name
            else:
                print('the given name does not exist, please enter again')

    def replace_df(self):
        main_df = pd.read_excel('./data.xlsx', sheet_name='Sheet1',usecols=['Room Number','Name','Phone'])
        df=main_df
        old_name= self.old_name()
        find_name = df[df['Name'] == old_name].index[0]
        new_name = str(input('Type the new person\'s name here: ')).upper()
        new_number = int(input('Type the new person\'s phone number here: '))
        changer_requestor = str(input('What is the name of the requestor?: '))
        df = df.replace((df.loc[find_name][1]), new_name)
        outputDF = df.replace((df.loc[find_name][2]), new_number)
 #this outputdf should be the input for your schedule creation sheet
        index_df = outputDF
        today = date(2022, 12, 26)
        dt = today + datetime.timedelta(days=-today.weekday(), weeks=0)

        a = {'room number': [], 'name': [], 'phone': [], 'date': []}
        for i in range(0, 200):
            for j in range(len(index_df['Room Number'])):
                dt = dt + datetime.timedelta(days=7)
                a['room number'].append(index_df['Room Number'][j])
                a['date'].append(dt)
                a['name'].append(index_df['Name'][j])
                a['phone'].append(index_df['Phone'][j])
        aa = pd.DataFrame(a)
#----logging the user_-------
        log_df = pd.read_excel('./data.xlsx', sheet_name='Log', usecols=['Date-Time','User/Changer','Old Name','New Name'])
        new=pd.DataFrame({'Date-Time':[datetime.datetime.now()],'User/Changer': [changer_requestor],'Old Name':old_name,'New Name': [new_name]})
        new_new = pd.concat([log_df,new])
        with pd.ExcelWriter('./data.xlsx') as writer:
            outputDF.to_excel(writer,sheet_name='Sheet1')  # this output df is your new df with replaced values
            aa.to_excel(writer,sheet_name='finalSchedule')
            new_new.to_excel(writer,sheet_name='Log')

c=schuyler()
c.replace_df()

#i just want to test this VScode integration to my git-----
