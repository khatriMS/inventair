let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 5.9,
    center: { lat: 21, lng: -8},
  });
  // NOTE: This uses cross-domain XHR, and may not work on older browsers.
  map.data.loadGeoJson(
    "",
  );
}
window.initMap = initMap;