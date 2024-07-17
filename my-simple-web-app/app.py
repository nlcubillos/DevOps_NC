from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Bienvenido a mi aplicación web</h1><p>Fecha y hora actuales: {formatted_date}</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
