# Import libraries
from matplotlib import pyplot as plt
import pandas as pd
import math
import plotly.express as px


def nutpie(csv_data, dailyCalVal, numDays=1):
    df = pd.read_csv(csv_data, usecols=['Date', 'Calories'])
    
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    df = df.groupby(by=df['Date'].dt.date).sum()

    df['CalPie']= df['Calories']/dailyCalVal
    # title = 'Calorie Intake %' + ' Over Last {} Days'.format(numDays),
    fig = px.pie( values=[df['CalPie'].iloc[-numDays:].mean(),1-df['CalPie'].iloc[-numDays:].mean()], hole=.3)

    # Change margins
    fig.update_layout(
        autosize=False,
        margin=dict(
            l=2,
            r=0,
            b=1,
            t=1,
            pad=2
        ),
    )
    # Change fig size and make background transparent
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', width=250, height=250)
    return fig

# nutpie('Nutrition.csv',2000, 10)