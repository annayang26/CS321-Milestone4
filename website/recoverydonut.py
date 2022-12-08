# Import libraries
from matplotlib import pyplot as plt
import pandas as pd
import math
import plotly.express as px


def recpie(csv_data, numDays=1):
    df = pd.read_csv(csv_data, usecols=['Recovery score %'])
    
    df['Recovery score %']= df['Recovery score %']/100
    print(df)
    # title = 'Recovery Score %' + ' Over Last {} Days'.format(numDays),
    fig = px.pie( values=[df['Recovery score %'].iloc[-numDays:].mean(),1-df['Recovery score %'].iloc[-numDays:].mean()], hole=.3)
    
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

# recpie('physiological cycles.csv', 3)