from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    return "Tu dirección IP es: " + request.remote_addr + "\n"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)