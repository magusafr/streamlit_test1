import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt

st.write("""
## New Cases Covid-19 in Indonesia
### Source: Ourworldindata.org
Visualisation by magusafr



""")

#my_func
def tgl_trx2(seriesdate):
  abc = [dt.datetime.strptime(str(i), '%Y-%m-%d') for i in seriesdate]
  return abc

new_cases = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
new_cases = new_cases[new_cases['location'] == 'Indonesia']
new_cases['date'] = tgl_trx2(new_cases['date'])
new_cases = new_cases.fillna(0)
df = new_cases.set_index('date')

st.line_chart(df['new_cases'], width=0, height=0, use_container_width=False)
