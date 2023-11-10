# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)
print("Server is running...")
@app.route('/api/findServices', methods=['POST'])
def find_services():
    try:
        print('Connection established to /api/findServices endpoint')
        data = request.get_json()
        print('Received Data:', data)
        location = data['location']
        radius = data['radius']

        # Your logic to find nearest fire stations and calculate shortest distance
        # ...

        # Example response
        nearest_station = {'lat': 33.8894627, 'lon': -84.5165133}
        shortest_distance_node = {'node_id': 123, 'distance': 1055.73}

        return jsonify({'nearestStation': nearest_station, 'shortestDistanceNode': shortest_distance_node})

    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
