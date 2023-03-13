from flask import Flask, render_template
import ngsiv2

app = Flask(__name__)

def list_inventory_items_for_product(product_id):
    status_code,data = ngsiv2.items_for_entity(product_id,"refProduct")
    if status_code == 200:
        return render_template('product_inventory_item.html',
                               inventoryitems = data)

def list_inventory_items_for_store(store_id):
    status_code,data = ngsiv2.items_for_entity(store_id,"refStore")
    if status_code == 200:
        return render_template('store_inventory_item.html',
                               inventoryitems = data)

@app.route("/")
def home():
    return render_template("home.html")

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
        return render_template('product.html', product = data) +\
        list_inventory_items_for_product(product_id)
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

@app.route('/Store/<store_id>')
def display_store(store_id):
    (status, data) = ngsiv2.read_entity(store_id)
    if status == 200:
        return render_template('store.html', store = data) +\
        list_inventory_items_for_store(store_id)
    else:
        return render_template('error.html',
        error = f"Error reading product {store_id}.\
                Orion response: {data}") 