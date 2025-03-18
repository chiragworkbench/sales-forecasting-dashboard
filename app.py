import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sales_data')
def get_sales_data():
    df = pd.read_csv('sales_data.csv')  # Load data from CSV
    data = {
        "month": df["month"].tolist(),
        "sales": df["sales"].tolist()
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
