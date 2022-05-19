// JavaScript to render Google map and put markers on map
// copied from Code Institute InteractiveFrontEndDevelopment-Resume

// Render map
function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: {
            lat: 36.617779,
            lng: -121.916664
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    var locations = [
        { lat: 36.617779, lng: -121.916664 }
    ];

    // Put markers at specified locations
    var markers = locations.map((location, i) => new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        })
    );

    // Cluster markers if necessary
    var markerCluster = new MarkerClusterer(map, markers);
}