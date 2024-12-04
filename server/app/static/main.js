const map = L.map('map').setView([0, 0], 2); // Default view

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

fetch('/api/locations')
    .then(response => response.json())
    .then(data => {
        data.forEach(location => {
            L.marker([location.latitude, location.longitude])
                .addTo(map)
                .bindPopup(`Lat: ${location.latitude}, Lon: ${location.longitude}, Alt: ${location.altitude}`);
        });
    });
