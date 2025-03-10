document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map').setView([43.529742, 5.447427], 14); // Coordinates for Aix-en-Provence, France

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([43.529742, 5.447427]).addTo(map)
        .bindPopup('Aix-en-Provence, France')
        .openPopup();
});