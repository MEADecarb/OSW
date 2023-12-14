# Maryland Geospatial Data Visualization for Offshore Wind

## Project Overview
This project is a Python-based interactive map visualization using the Folium library. It focuses on visualizing two key aspects of Maryland's geography: Offshore Wind Energy Planning and Maryland's County Boundaries. The map is enhanced with a custom color palette and an interactive legend, providing a clear and informative view of the geospatial data.

## Features
- Interactive map centered over Maryland.
- GeoJSON layers for Offshore Wind Energy Planning and MDOT SHA County Boundaries.
- Custom color palette for distinct visualization of different layers.
- Interactive legend detailing the color coding of the map layers.
- Pop-ups on each layer providing detailed information about the selected feature.

## Technology
- Python
- Folium: A Python library used for visualizing geospatial data.
- GeoJSON: A format for encoding a variety of geographic data structures.

## Setup and Installation
Ensure you have Python installed on your system. Then, install the required packages:

```bash
pip install folium requests
```

## Usage
To run the visualization, execute the Python script. This will render an interactive map in a web browser.

```python
# Run the script
python map_visualization.py
```

## Contributing
Contributions to this project are welcome. Feel free to fork the repository and submit pull requests.

## License
This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements
Data sources:
- Offshore Wind Energy Planning: [GeoJSON Source](https://geodata.md.gov/imap/rest/services/UtilityTelecom/MD_OffshoreWindEnergyPlanning/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson)
- MDOT SHA County Boundaries: [GeoJSON Source](https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MDOT_SHA_County_Boundaries/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson)

## Contact
For any questions or comments, please feel free to reach out.
