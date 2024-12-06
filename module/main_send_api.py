import requests
from pynmeagps import NMEAReader
import serial

def parse_gngga_sentence(nmea_sentence):
    """
    Parses a GNGGA sentence to extract latitude, longitude, and altitude.
    """
    parts = nmea_sentence.split(',')
    if len(parts) < 10:
        return None  # Invalid sentence

    # Latitude
    try:
        lat = float(parts[2][:2]) + float(parts[2][2:]) / 60.0
        if parts[3] == 'S':
            lat = -lat
        # Longitude
        lon = float(parts[4][:3]) + float(parts[4][3:]) / 60.0
        if parts[5] == 'W':
            lon = -lon
        # Altitude
        alt = float(parts[9]) if parts[9] else 0.0
    except ValueError:
        return None  # Handle parsing errors

    return lat, lon, alt

def read_gps_data(serial_port='/dev/ttyS0', baudrate=115200):
    """
    Reads GPS data from the serial port and extracts GNGGA sentences.
    """
    with serial.Serial(serial_port, baudrate, timeout=3) as stream:
        nmr = NMEAReader(stream)
        while True:
            try:
                (raw_data, parsed_data) = nmr.read()
                if bytes("GNGGA", 'ascii') in raw_data:
                    return raw_data.decode('ascii')
            except Exception as e:
                print(f"Error reading GPS data: {e}")
                return None

def send_location_to_api(self, latitude, longitude, api_url):
    """
    Sends location data to the specified API endpoint via POST request.
    """
    data = {"latitude": latitude, "longitude": longitude}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()
        print(f"Location sent successfully: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send location data: {e}")

def main():
    """
    Main function to read GPS data, parse location, and send it to the API.
    """
    api_url = "100.77.9.22"

    while True:
        nmea_sentence = read_gps_data()
        if nmea_sentence:
            print(f"NMEA Sentence: {nmea_sentence}")
            location = parse_gngga_sentence(nmea_sentence)
            if location:
                lat, lon, _ = location
                print(f"Parsed Location: Latitude={lat}, Longitude={lon}")
                send_location_to_api(lat, lon, api_url)
            else:
                print("Failed to parse NMEA sentence.")
        else:
            print("No NMEA data received.")

if __name__ == "__main__":
    main()
