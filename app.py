from flask import Flask, jsonify
from faker import Faker

faker = Faker()

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Faker api"

@app.route("/generate_names/<amount>", methods=['GET'])
def get_names(amount):
        item_list = []
        for i in range(int(amount)):
            item_list.append(faker.name())
        return jsonify(item_list)

@app.route("/generate_addresses/<amount>", methods=['GET'])
def generate_addresses(amount):
            item_list = []
            for i in range(int(amount)):
                item_list.append(faker.address())
            return jsonify(item_list)