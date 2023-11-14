
#Name: Amaya Mangual
#Date: November 23

import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.768731, -73.125], popup = "Hunter College").add_to(mapCUNY)

mapCUNY.save(outfile='nycMap.html')
