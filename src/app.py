from flask import Flask
from flask import jsonify
from flask import render_template
import socket

app = Flask(__name__)

# Function to fetach hostname and ip 
def get_Host_Name_IP():
        host_name = socket.gethostname()
        host_ip = "10.76.184.100"
        return str(host_name), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )
    
@app.route("/details")
def details(name=None):
    hostname, ip = get_Host_Name_IP()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)