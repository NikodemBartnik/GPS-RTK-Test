from flask import Flask, request, jsonify, render_template
from models import db, Location
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/api/location', methods=['POST'])
def save_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    altitude = data.get('altitude', 0.0)  # Optional field

    if latitude is None or longitude is None:
        return jsonify({'error': 'Latitude and Longitude are required'}), 400

    location = Location(latitude=latitude, longitude=longitude, altitude=altitude)
    db.session.add(location)
    db.session.commit()
    return jsonify({'message': 'Location saved successfully!'}), 201

@app.route('/api/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    data = [{'latitude': loc.latitude, 'longitude': loc.longitude, 'altitude': loc.altitude} for loc in locations]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
