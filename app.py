from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Wireless Keyboard", "category": "Electronics", "price": 18.99},
    {"name": "Office Mouse", "category": "Electronics", "price": 9.99},
    {"name": "Storage Boxes", "category": "Office Supplies", "price": 12.50},
    {"name": "LED Desk Lamp", "category": "Lighting", "price": 21.99}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
