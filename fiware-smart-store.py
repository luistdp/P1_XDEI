from flask import Flask, render_template, redirect,url_for,request
import ngsiv2
import ast

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
    
@app.route('/Subscriptions')
def subscriptions():
    (status, subscriptions_data) = ngsiv2.read_subcriptions()
    return render_template("subscriptions.html", subscriptions = subscriptions_data,
                           modify_base_url = "/Subscriptions/Modify/")

@app.route("/Subscription/Delete/<subscription_id>", methods = ["POST"])
def delete_subscription(subscription_id):
    status = ngsiv2.delete_subscription(subscription_id)
    if status == 204:
        return redirect(url_for("subscriptions"))
    
@app.route("/Subscription/Modify/<subscription_id>", methods = ["GET","POST"])
def modify_subscription(subscription_id):
    (status,data) = ngsiv2.read_subscription(subscription_id)
    if status == 200:
        if request.method == 'POST':
            if len(request.form['description']) == 0:
                description = data["description"]
            else:
                description = request.form["description"]
            if len(request.form['entity_id']) == 0:
                entities_id_pattern = data["subject"]["entities"][0]["idPattern"]
            else:
                entities_id_pattern = request.form["entity_id"]
            if len(request.form["condition_attrs"]) == 0:
                condition_attrs = data["subject"]["condition"]["attrs"]
            else:
                condition_attrs = request.form["condition_attrs"]
            if len(request.form["httpurl"]) == 0:
                httpurl = data["notification"]["http"]["url"]
            else:
                httpurl = request.form["httpurl"]
            if len(request.form["attributes"]) == 0:
                attributes = data["notification"]["attributes"]
            else:
                attributes = request.form["attributes"]
            if len(request.form["metadata"]) == 0:
                metadata = data["notification"]["metadata"]
            else:
                metadata = request.form["metadata"]
            
            modification ={
                "description":description,
                "subject":{
                    "entities":[
                        {
                            "idPattern":entities_id_pattern
                        }
                    ],
                    "condition":{
                        "attrs":ast.literal_eval(condition_attrs)
                    }
                },
                "notification":{
                    "attrs":ast.literal_eval(attributes),
                    "http":{
                        "url":httpurl
                    },
                    "metadata":ast.literal_eval(metadata)
                }
                }
            if len(request.form["throttling"]) != 0:
                modification["throttling"] = int(request.form["throttling"])
                s = ngsiv2.update_subscription(subscription_id, modification)
            else:
                s =  ngsiv2.update_subscription(subscription_id,modification)
                        
            return redirect(url_for('subscriptions'))
        else:
            return render_template('modify_subscriptions.html', subscription_id = subscription_id)

@app.route("/Subscription/Create", methods = ["GET","POST"])
def create_subscription():
    if request.method == 'POST':
        body ={
            "description":request.form["description"],
            "subject":{
                "entities":[
                    {
                        "idPattern":request.form["entity_id"]
                    }
                ],
                "condition":{
                    "attrs":ast.literal_eval(request.form["condition_attrs"])
                }
            },
            "notification":{
                "attrs":ast.literal_eval(request.form["attributes"]),
                "http":{
                    "url":request.form["httpurl"]
                },
                "metadata":ast.literal_eval(request.form["metadata"])
            }
        }
        if len(request.form["throttling"]) != 0:
            body["throttling"] = int(request.form["throttling"])
            s = ngsiv2.create_subscription(body)
        else:
            s =  ngsiv2.create_subscription(body)

        return redirect(url_for('subscriptions'))
    else:
        return render_template('create_subscription.html')