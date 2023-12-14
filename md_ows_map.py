import folium
import json
import requests
from branca.element import Template, MacroElement

# Function to add GeoJSON from a URL to a feature group with custom color and pop-up
def add_geojson_from_url(geojson_url, name, color, map_obj):
    feature_group = folium.FeatureGroup(name=name)
    style_function = lambda x: {'fillColor': color, 'color': color}
    response = requests.get(geojson_url)
    geojson_data = response.json()

    geojson_layer = folium.GeoJson(
        geojson_data,
        style_function=style_function
    )

    if name == "Offshore Wind Energy Planning":
        fields = ['PROT_NUMBE', 'PROT_APRV_', 'BLOCK_NUMB', 'BLK_FED_AP', 'BLOCK_LAB', 'SUB_BLK']
        aliases = ['Protraction Number', 'Protraction Approval', 'Block Number', 'Block Approval', 'Block Label', 'SubBlock']
        geojson_layer.add_child(folium.GeoJsonPopup(fields=fields, aliases=aliases, labels=True))
    elif name == "MDOT SHA County Boundaries":
        geojson_layer.add_child(folium.GeoJsonPopup(fields=['COUNTY_NAME'], aliases=['County:'], labels=True))
    else:
        all_fields = list(geojson_data['features'][0]['properties'].keys())
        geojson_layer.add_child(folium.GeoJsonPopup(fields=all_fields, labels=True))

    geojson_layer.add_to(feature_group)
    feature_group.add_to(map_obj)

# Function to add a legend to the map
def add_legend(map_obj, color_palette, labels):
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 150px; height: 90px; 
                border:2px solid grey; z-index:9999; font-size:14px;
                ">&nbsp; <b>Legend</b> <br>
                &nbsp; {0} &nbsp; <i style="background:{1};opacity:0.7;"></i><br>
                &nbsp; {2} &nbsp; <i style="background:{3};opacity:0.7;"></i><br>
                &nbsp; {4} &nbsp; <i style="background:{5};opacity:0.7;"></i><br>
    </div>
    '''.format(labels[0], color_palette[0], 
               labels[1], color_palette[1], 
               labels[2], color_palette[2])

    legend = MacroElement()
    legend._template = Template(legend_html)

    map_obj.get_root().add_child(legend)

# Define a color palette
color_palette = ["#2C557E", "#fdda25", "#B7DCDF", "#000000"]

# Create a base map centered over Maryland
m = folium.Map(location=[39.0458, -76.6413], zoom_start=8)

# Add each GeoJSON source as a separate feature group with a color, label, and pop-up
github_geojson_sources = [
    ("https://geodata.md.gov/imap/rest/services/UtilityTelecom/MD_OffshoreWindEnergyPlanning/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson", "Offshore Wind Energy Planning"),
    ("https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MDOT_SHA_County_Boundaries/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson", "MDOT SHA County Boundaries")
]

for i, (url, name) in enumerate(github_geojson_sources):
    color = color_palette[i % len(color_palette)]
    add_geojson_from_url(url, name, color, m)

# Define labels for your legend (these should correspond to your layers)
legend_labels = ["Offshore Wind Energy Planning", "MDOT SHA County Boundaries", "Other Layer"]

# Add legend to the map
add_legend(m, color_palette, legend_labels)

# Display the map
m
