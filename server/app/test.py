import requests

def post_predefined_location():
    url = 'http://localhost:5000/api/location'
    predefined_locations = [
        {'latitude': 41.3128, 'longitude': -71.5060, 'altitude': 1},  # New York
        {'latitude': 42.4128, 'longitude': -72.8060, 'altitude': 1},  # Los Angeles
        {'latitude': 43.2128, 'longitude': -75.2060, 'altitude': 1},  # London
        {'latitude': 44.5128, 'longitude': -72.5060, 'altitude': 1}  # Tokyo
    ]

    for location in predefined_locations:
        response = requests.post(url, json=location)
        if response.status_code == 201:
            print('Location saved successfully!')
        else:
            print(f'Failed to save location: {response.json()}')

if __name__ == "__main__":
    post_predefined_location()