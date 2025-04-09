from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def validate_input(json_data):
    if not json_data:
        return "Invalid request format"
    if 'number1' not in json_data:
        return "Missing number1 field"
    if 'number2' not in json_data:
        return "Missing number2 field"
    if 'operation' not in json_data:
        return "Missing operation field"
    if not isinstance(json_data['number1'], int):
        return "Invalid number1 data type"
    if not isinstance(json_data['number2'], int):
        return "Invalid number2 data type"
    if json_data['operation'] not in ['+', '-', '*', '/']:
        return f"Invalid operation character {json_data['operation']}"
    return None

def calculate_result(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        return round(number1 / number2, 2)

@app.route('/calculate', methods=['POST'])
def calculate():
    json_data = request.json
    validation_error = validate_input(json_data)
    if validation_error:
        return jsonify({"errorMessage": validation_error}), 400

    number1 = json_data['number1']
    number2 = json_data['number2']
    operation = json_data['operation']
    
    result = calculate_result(number1, number2, operation)
    return jsonify({"result": str(result)}), 200

if __name__ == '__main__':
    app.run(host="192.168.1.6", port=65000, debug=True)



