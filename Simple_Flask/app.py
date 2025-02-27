from flask import Flask, request


app = Flask(__name__)


stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name":"Chair",
                "price":15.99
            }
        ]
    }
]

@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"store":stores}

@app.post("/store") #http://127.0.0.1:5000/store
def create_store():
    request_data = request.get_json()
    new_store = {
        "name":request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item") #http://127.0.0.1:5000/store/My 2nd Store/item
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"], "price":request_data["price"] }
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not exist"}, 404

@app.get("/store/<string:name>") #http://127.0.0.1:5000/store/My 2nd Store
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 201
    return {"message":"Store not exist"}, 404

@app.get("/store/<string:name>/item") #http://127.0.0.1:5000/store/My 2nd Store/item
def get_store_item(name):
    for store in stores:
        if store["name"] == name:
            return {"items":store["items"]}, 201
    return {"message":"Store not exist"}, 404

@app.put("/store/<string:name>") #http://127.0.0.1:5000/store/My 2nd Store
def update_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            store["name"] = request_data.get("name", store["name"])
            store["items"] = request_data.get("items", store["items"])
            return {"message": "Store updated successfully", "store": store}, 201
    return {"message": "Store not found"}, 404

@app.delete("/store/<string:name>") #http://127.0.0.1:5000/store/My Store 2
def delete_store(name):
    global stores
    stores = [store for store in stores if store["name"] != name]
    return {"message": "Store deleted"}, 401
