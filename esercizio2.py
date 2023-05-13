from flask import Flask, request, render_template
import geopandas as gpd
import pandas as pd
app = Flask(__name__)

df = pd.read_excel("https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true")
df

@app.route('/')
def home():
    quartieri = df['neighborhood']
    quartieri_sort = quartieri.sort_values()
    quartieri_sort = list(dict.fromkeys(quartieri_sort))
    return render_template('es2.html', quartiere = quartieri_sort)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)