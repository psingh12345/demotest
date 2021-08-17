from django.shortcuts import render
from django.http.response import HttpResponse
import pandas as pd

db_engine = 'postgresql://postgres:SqQa0HlywiyLEYpU7Egd@13.126.171.123:5432/testdb'
print('Sucess')

username = 'rohit'
password = 'fuck'
    
from sqlalchemy import create_engine
engine = create_engine(db_engine)
    
dataentries = pd.read_sql_query('Select * from "testlogin"', con=engine)

print(dataentries['username'])

    