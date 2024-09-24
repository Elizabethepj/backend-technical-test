from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import uuid
from error_handler import handle_error

load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
    return "backend-technical-test"


# Simulación de una base de datos de contactos
contacts = {
    "1": {"name": "Alice", "email": "alice@example.com"},
    "2": {"name": "Bob", "email": "bob@example.com"},
    "3": {"name": "Elizabeth", "email": "eli@example.com"},
}

# Ruta para obtener información de contacto. Se usa un GET


@app.route('/contacts/<contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = contacts.get(contact_id)
    if contact:
        return jsonify(contact), 200
    return jsonify({"error": "Contact not found"}), 404

# Ruta para autenticar usuarios (simulada)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400

    # Simulando autenticación
    if data['username'] != 'admin':
        return jsonify({"error": "User does not exist"}), 403
    if data['password'] != 'secret':
        return jsonify({"error": "Incorrect password"}), 401

    return jsonify({"message": "Login successful"}), 200

# Método para manejar productos (simulado). Se usa GET


@app.route('/products', methods=['GET'])
def loop_products_and_parse():
    products = [
        {"id": uuid.uuid4(), "name": "Product 1"},
        {"id": uuid.uuid4(), "name": "Product 2"}
    ]
    return jsonify(products), 200


if __name__ == '__main__':
    app.run(debug=True)
