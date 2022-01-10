from flask import Flask, render_template
import sqlite3
import pandas as pd
import json
import plotly
import plotly.express as px

con = sqlite3.connect("DHT_data.db")
df = pd.read_sql_query("SELECT * from DHT_data", con)
print(df)

app = Flask(__name__)

@app.route('/')

def graph():

    fig1 = px.line(df, x='timestamp', y='hum')
    fig2 = px.line(df, x='timestamp', y='temp')

    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON1=graphJSON1, graphJSON2=graphJSON2)

if __name__ == "__main__":
    app.run(debug=True)

