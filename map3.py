import folium
import matplotlib.pyplot as plt

# Create a Folium map
map_center = [12, 12]
map_zoom = 12
map_osm = folium.Map(location=map_center, zoom_start=map_zoom)

# Adding markers to the map
marker_coords = [12, 12]
folium.Marker(location=marker_coords, popup='Marker Popup Text').add_to(map_osm)
# Save the Folium map as an HTML file
map_html = 'map_osm.html'
map_osm.save(map_html)

# Read the HTML content
with open(map_html, 'r') as file:
    map_content = file.read()

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(8, 6))

# Display the map using Matplotlib's plot function
ax.plot([0, 1])  # You can add other elements to the Matplotlib plot as needed
ax.imshow(map_content, interpolation='none', aspect='auto')
ax.axis('off')

# Show the plot
plt.show()