import csv
import pandas as pd

def sleepcsv():
    df = pd.read_csv('website/data/sleep.csv', usecols=['Cycle start time', 'Sleep performance %', 'Asleep duration (min)'])

    # df['Cycle start time'] = pd.to_datetime(df['Cycle start time'], errors='coerce')
    df['Asleep duration (min)'] = round(df['Asleep duration (min)']/60, 1)
    print(df)

    csvfile = df.to_csv()
    return csvfile



# print(csvfile)