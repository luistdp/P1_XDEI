from flask import Flask, render_template
import ngsiv2

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/Products")
def products():
    _, products = ngsiv2.list_entities(type="Product")
    return render_template("products.html",
                           products = products,
                           product_base_url = '/Product/')

@app.route('/Product/<product_id>')
def display_product(product_id):
    (status, data) = ngsiv2.read_entity(product_id)
    if status == 200:
        return render_template('product.html', product = data)
    else:
        return render_template('error.html',
        error = f"Error reading product {product_id}.\
                Orion response: {data}") 

@app.route("/Stores")
def stores():
    _,stores = ngsiv2.list_entities(type="Store")
    return render_template("stores.html",
                           stores = stores,
                           store_base_url = '/Store/')