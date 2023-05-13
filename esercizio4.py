from flask import Flask, request, render_template
import geopandas as gpd
import pandas as pd
app = Flask(__name__)

df = pd.read_excel("https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true")
df

@app.route('/')
def home():
  quartieri = df['neighborhood']
  return render_template('es4.html', quartiere = quartieri)

@app.route('/prezzo', methods = ["GET"])
def prezzo():
  quartieri = request.args.get('Quartiere')
  cquart = df[df['neighborhood'] == quartieri]
  cquart = cquart.price.mean()      
  return render_template('ris.html', pmed = cquart, quart = quartieri)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)