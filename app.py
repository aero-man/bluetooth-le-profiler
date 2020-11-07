from flask import Flask, render_template

from device_database import BluetoothDeviceDatabase


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! 123'

@app.route('/otherpage')
def other_page():
    return 'This is another page'

@app.route('/devices')
def device_index():
    bdd = BluetoothDeviceDatabase()
    devices = bdd.cursor.execute('SELECT * FROM devices;')
    return str(devices.fetchall())

@app.route('/devices-formatted')
def devices_formatted():
    bdd = BluetoothDeviceDatabase()
    devices = bdd.cursor.execute('SELECT * FROM devices;').fetchall()
    print(type(devices))
    return render_template('devices.html', devices=devices)


