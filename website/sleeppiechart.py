# Import libraries
from matplotlib import pyplot as plt
import pandas as pd
import math
import plotly.express as px


def sleeppie(csv_data, numDays=1):
    df = pd.read_csv(csv_data, usecols=['Sleep performance %'])

    df['Sleep performance %']= df['Sleep performance %']/100

    fig = px.pie( values=[df['Sleep performance %'].iloc[-numDays:].mean(),1-df['Sleep performance %'].iloc[-numDays:].mean()], hole=.3)
    
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