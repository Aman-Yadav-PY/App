from flask import Flask 
import os

app = Flask(__name__)

@app.route('/')
def hello():
	return "First Program"

port = int(os.getenv('PORT', 5000))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port, debug=True)