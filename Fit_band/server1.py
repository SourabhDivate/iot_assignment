from flask import Flask, request
from utils.database import execute_query
from utils.database import execute_select_query
import paho.mqtt.client as mqtt

add = Flask(__name__)

def on_publish(methods, status):
    print("Message is published\n")
    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.connect("mqtt.eclipseprojects.io")
    message = f"{methods} : {status}"
    publisher.publish("health/status", message)
    publisher.disconnect()

@add.route('/add', methods = ['POST'])
def add_user():
    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.on_publish = request.method

    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')
    steps = request.form.get('steps')
    pulse = request.form.get('pulse')
    oxygen = request.form.get('oxygen')
    temperature = request.form.get('temperature')
    query = f"insert into health (name, age, city, steps, pulse, oxygen, temperature) values ('{name}', {age}, '{city}', {steps}, {pulse}, {oxygen}, {temperature});"
    execute_query(query)
    on_publish("add", "success")
    return f"{name} inserted successfully"

@add.route('/all', methods = ['GET'])
def all_user():
    query = f"select * from health;"
    user = execute_select_query(query)
    on_publish("all", "success")
    return user

@add.route('/info', methods = ['GET'])
def user_info():
    name = request.form.get('name')
    query = f"select * from health where name = '{name}';"
    user = execute_select_query(query)
    on_publish("info", "success")
    return user

@add.route('/update', method = ['PUT'])
def update_city():
    name = request.form.get('name')
    city = request.form.get('city')
    query = f"update into health SET city = '{city}' where name = '{name}';"
    execute_query(query)
    on_publish("update", "success")
    return f"{name} updated successfully"

@add.route('/maximum', methods = ['GET'])
def maximim_step():
    query = f"select * from health where steps = (select MAX(steps) from health)"
    user = execute_select_query(query)
    on_publish("maximum", "success")
    return user

if __name__ == "__main__":
    add.run(debug = True)