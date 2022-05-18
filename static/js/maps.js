function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 3,
        center: {
            lat: 38.5,
            lng: -100
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    var locations = [
        { lat: 36.617779, lng: -121.916664 }
    ];

    var markers = locations.map((location, i) => new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        })
    );

    var markerCluster = new MarkerClusterer(map, markers);
}