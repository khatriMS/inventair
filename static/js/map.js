// map.js

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: { lat: -28, lng: 137 },
    });

    // Load GeoJSON data
    map.data.loadGeoJson("https://storage.googleapis.com/mapsdevsite/json/google.json");
}

window.initMap = initMap;