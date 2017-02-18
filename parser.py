import os,sys
import pandas as pd

def remove_empty(arr):
    out = []
    for item in arr:
        if item != '' and item != ' ':
            out.append(item)
    return out

def get_data():
    headers = ['cad','date','time','addr','incident','officer','unit']
    out = []
    for item in os.listdir('data/'):
        f = open('data/{}'.format(item)).read().split('\r\n')
        for row in f:
            r = remove_empty(row.split('   '))
            if r != []:
                out.append(r)

    df = pd.DataFrame(out,columns=headers)
    df.to_csv('out.csv')

get_data()
