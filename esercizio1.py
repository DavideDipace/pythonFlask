from flask import Flask, request, render_template
import geopandas as gpd
import pandas as pd
app = Flask(__name__)

df = pd.read_excel("https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true")
df

testpoli = gpd.read_file("province2.zip") #caricare dati da drive
testpoli

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/tabella', methods=['GET', 'POST'])
def tab():
    return render_template('test.html', table = df.to_html())

@app.route('/data', methods=['GET', 'POST'])
def data():
    quartiere = request.args.get('quartiere')
    Quartiere = df[df['neighborhood'] == quartiere]
    Quartiere_sort = Quartiere.sort_values("date")
    return render_template('riepilogo.html', quartiere=Quartiere_sort.to_html())#per rappresentare una tabella usare il metodo .to_html()
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)