from flask import Flask, jsonify
from faker import Faker

faker = Faker()

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Faker api"

@app.route("/get_names")
def get_names():
    names = []
    for i in range(100):
        names.append(faker.name())
    return jsonify(names)