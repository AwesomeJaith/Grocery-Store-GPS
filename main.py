from map import Map
from flask import Flask, request, render_template, jsonify, send_from_directory
from pydantic import BaseModel
import os
import json

app = Flask(__name__)

class GroceryList(BaseModel):
    groceries: list[str]

result = None

def generate_store(store):
    store_map_model = Map(store)
    return store_map_model

def calculate_optimal_path(grocery_list, store_map_model):
    store_map = store_map_model
    optimal_path = store_map.find_optimal_path(grocery_list)
    image_path = generate_image(optimal_path, store_map)

    result = {
        "optimal_path": optimal_path,
        "image_name": image_path
    }
    
    return result

def generate_image(optimal_path, store_map_model):
    store_map = store_map_model
    image_path = store_map.draw_path_png(optimal_path, "static")
    return image_path


@app.route("/")
def index():
    return "Hello, World!"

@app.route("/api")
def api():
    return render_template("index.html")

@app.route("/api/calculate-optimal-path", methods=["GET", "POST"])
def get_optimal_path():
    if request.method == "GET":
        context = {"title": "calculate optimal path", "route": "/api/calculate-optimal-path", "description": "This endpoint serves you a list with the optimal path through the Woodman's Store in Carpentersville, Illinois given a specific grocery list."}
        return render_template("route_template.html", **context)
    if request.method == "POST":
        try:
            data = request.json

            if "groceries" in data:
                grocery_list = data["groceries"]
                store_model = generate_store("woodmans_carpentersville_map_data.json")
                result = calculate_optimal_path(grocery_list, store_model)
                optimal_path = result["optimal_path"]

                json_file_path = os.path.join(app.static_folder, 'temp.json')
                
                with open(json_file_path, 'w') as json_file:
                    json.dump(result, json_file, indent=4)

                return jsonify({"optimal_path": optimal_path}), 200
            else:
                return jsonify({"error": "Missing 'groceries' in request data"})

        except Exception as e:
            return jsonify({"error": "An error occurred"}), 500

@app.route("/api/calculate-optimal-path/image", methods=["GET"])
def get_image():
    if request.method == "GET":
        try:
            return render_template("image_template.html"), 200
        except Exception as e:
            return jsonify({'error': 'Image not found!'}), 500

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500