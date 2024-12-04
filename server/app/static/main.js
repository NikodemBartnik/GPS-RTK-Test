const map = L.map('map').setView([0, 0], 2); // Default view

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

fetch('/api/locations')
    .then(response => response.json())
    .then(data => {
        const latlngs = data.map(location => [location.latitude, location.longitude]);
        L.polyline(latlngs, { color: 'blue' }).addTo(map);
    });
