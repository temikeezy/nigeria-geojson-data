import json
import folium
from folium.plugins import MarkerCluster

# Load your data from a JSON file
with open("wards.json", "r") as f:
    data_points = json.load(f)

# Convert to GeoJSON format
geojson_data = {
    "type": "FeatureCollection",
    "features": []
}

for point in data_points:
    feature = {
        "type": "Feature",
        "properties": {
            "State": point["State"],
            "LGA": point["LGA"],
            "Ward": point["Ward"]
        },
        "geometry": {
            "type": "Point",
            "coordinates": [point["Longitude"], point["Latitude"]]
        }
    }
    geojson_data["features"].append(feature)

# Create a folium map
first_lat = data_points[0]["Latitude"]
first_lon = data_points[0]["Longitude"]
map_obj = folium.Map(location=[first_lat, first_lon], zoom_start=10)

# Add points using marker clusters
marker_cluster = MarkerCluster().add_to(map_obj)
for feature in geojson_data["features"]:
    coords = feature["geometry"]["coordinates"]
    props = feature["properties"]
    popup = f"{props['Ward']}, {props['LGA']}, {props['State']}"
    folium.Marker(
        location=[coords[1], coords[0]],
        popup=popup,
        tooltip=popup
    ).add_to(marker_cluster)

# Save outputs
map_obj.save("geotagged_map.html")
with open("geotag_points.geojson", "w") as f:
    json.dump(geojson_data, f, indent=2)

print("✅ Map saved as geotagged_map.html")
print("✅ GeoJSON saved as geotag_points.geojson")
