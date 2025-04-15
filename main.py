from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/upload', methods=['POST'])
def upload_data():
    data = request.get_json()
    doc_ref = db.collection('sensorData').add(data)
    return jsonify({"success": True, "id": doc_ref[1].id})
