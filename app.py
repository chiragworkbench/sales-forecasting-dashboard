from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sales_data")
def sales_data():
    data = {
        "month": ["Jan", "Feb", "Mar"],
        "sales": [1000, 1500, 2000]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
