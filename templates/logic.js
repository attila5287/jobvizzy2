// Create a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: API_KEY
}).addTo(myMap);

// Define a markerSize function that will give each city a different radius based on its salary
function markerSize(salaryEstimated) {
  return salaryEstimated;
}

// Each city object contains the city's name, location and salaryEstimated
var cities = [{
    name: "New York",
    location: [40.7128, -74.0059],
    salaryEstimated: 118139
  },
  {
    name: "Chicago",
    location: [41.8781, -87.6298],
    salaryEstimated: 105602
  },
  {
    name: "Houston",
    location: [29.7604, -95.3698],
    salaryEstimated: 97884
  },
  {
    name: "Los Angeles",
    location: [34.0522, -118.2437],
    salaryEstimated: 122674
  },
  {
    name: "Omaha",
    location: [41.2524, -95.9980],
    salaryEstimated: 89107
  }
];

// Loop through the cities array and create one marker for each city object
for (var i = 0; i < cities.length; i++) {
  L.circle(cities[i].location, {
    fillOpacity: 0.75,
    color: "white",
    fillColor: "purple",
    // Setting our circle's radius equal to the output of our markerSize function
    // This will make our marker's size proportionate to its salaryEstimated
    radius: markerSize(cities[i].salaryEstimated)
  }).bindPopup("<h4>" + cities[i].name + "</h4> <hr> <h4>salaryEstimated: " + 0.001 * cities[i].salaryEstimated + "</h4>").addTo(myMap);
}