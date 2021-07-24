# find-route-webapp-in-django

Main idea:

Many emergency vehicles get stuck in the traffic. If the traffic control stations already knows about the arrival of ambulance they prepare the traffic according to it.
in emergency situations it is impossible to manually inform to all such places.
It is a short attempt to automate this process and helps to reduce the time delay of emergency vehicles.

when a call arrives it finds the shortest route between the points and shows it in a map.
It alerts all traffic control stations in that particular route about the vehicle and approximate time.

Status: In progress

Working features:
show map in browser using Leaflet.js 
admins can include locations to the database(in this case hospitals and traffic stations)
show shortest route from source to destination.
Query nearest hospital

Technologies used:
Django
Postgresql database with Postgis extension for storing spatial data
Openstreet map
Folium
Leaflet.js
