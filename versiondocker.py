from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    ip_cliente = request.remote_addr
    return f"La conexión se está realizando desde: {ip_cliente}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)