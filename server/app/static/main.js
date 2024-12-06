const map = L.map('map').setView([52.237049, 21.017532], 6); // Centered on Poland

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

let polyline = L.polyline([], { color: 'blue' }).addTo(map);

function fetchAndUpdate() {
    fetch('/api/locations')
        .then(response => response.json())
        .then(data => {
            const latlngs = data.map(location => [location.latitude, location.longitude]);
            polyline.setLatLngs(latlngs);
            map.fitBounds(polyline.getBounds()); // Zoom in on the added lines
        });
}

// Fetch and update every 3 seconds
setInterval(fetchAndUpdate, 3000);

// Initial fetch
fetchAndUpdate();
