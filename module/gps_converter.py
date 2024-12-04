import gpxpy
import gpxpy.gpx

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


def nmea_to_gpx(nmea_file, gpx_file):
    """
    Converts NMEA GNGGA data to GPX format.
    """
    gpx = gpxpy.gpx.GPX()
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    with open(nmea_file, 'r') as file:
        for line in file:
            if line.startswith('$GNGGA'):
                data = parse_gngga_sentence(line)
                if data:
                    lat, lon, alt = data
                    # Add the GPS point to the GPX track
                    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon, alt))

    # Write the GPX output
    with open(gpx_file, 'w') as file:
        file.write(gpx.to_xml())


# Example Usage
# Convert an NMEA file to GPX
nmea_file = 'F://gpsdata.txt'  # Replace with your NMEA file path
gpx_file = 'F://output.gpx'  # Desired output GPX file path
nmea_to_gpx(nmea_file, gpx_file)

print(f"Converted {nmea_file} to {gpx_file}.")
