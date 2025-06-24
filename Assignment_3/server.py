from flask import Flask,request
from utility.database import execute_query,execute_select_query
import paho.mqtt.client as mqtt
add=Flask(__name__)
def on_publish(method,status):
    print("message is publish\n")
    publisher=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.connect("mqtt.eclipseprojects.io")
    message=f"{method} : {status}"
    publisher.publish("health/status",message)

    publisher.disconnect()

@add.route('/add',methods=['POST'])

def add_user():
    publisher=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    publisher.on_publish =request.method


    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')
    steps = request.form.get('steps')
    pulse = request.form.get('pulse')
    oxygen = request.form.get('oxygen')
    temperature = request.form.get('temperature')
    query =f"insert into health (name, age, city, steps, pulse, oxygen, temp) values('{name}', {age}, '{city}', {steps}, {pulse}, {oxygen}, {temperature});"
    execute_query(query)
    on_publish("add","success")

    
    return f"{name} inserted succesfully"

@add.route("/all",methods=['GET'])
def all_user():
    query=f"select * from health;"
    user=execute_select_query(query)
    on_publish("all","success")

    return user

@add.route("/info",methods=['GET'])
def info_user():
    name=request.form.get('name')
    query=f"select * from health where name = '{name}';"
    user=execute_select_query(query)
    on_publish(request.method,"success")
    return user

@add.route("/update",methods=['POST'])
def update_user():
    name=request.form.get('name')
   
    city=request.form.get('city')
    
    query = f"update health SET city = '{city}' where name = '{name}';"
    execute_query(query)
    on_publish(request.method,"success")
    return f"{name} update succesfully"

@add.route("/steps",methods=['GET'])
def steps_user():
    on_publish(request.method,"success")
    query=f"select * from health order by steps DESC limit 1;"
    user=execute_select_query(query)
    
    return user
if __name__=="__main__":
    add.run(debug=True)





    

