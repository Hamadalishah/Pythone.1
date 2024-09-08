from flask import Flask, jsonify
from typing import Dict

app = Flask(__name__)

# Corrected type annotation for the dictionary
data: Dict[str, str] = {
    "Card": "Piaic",
    "Father Name": "Ali Asghar Shah",
    "Name": "Syed Muhammad Hamad Ali Shah",
    "Education": "BS Software Engineering",
    "Age": "24",
    "Roll No": "37466"
}

@app.route('/')
def home():
    resp = jsonify(data)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
