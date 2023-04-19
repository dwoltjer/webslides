import pandas as pd
import folium


def demo_folium_map():

    # create a map centered on the Netherlands
    netherlands_map = folium.Map(location=[52.1326, 5.2913], zoom_start=8, width='100%')

    # add the layer with the country capital (Amsterdam)
    capitals_df = pd.DataFrame({
        'city': ['Amsterdam', 'Rotterdam', 'Utrecht', 'The Hague', 'Groningen', 'Arnhem', 'Maastricht', 'Assen',
                 'Leeuwarden', 'Haarlem'],
        'lat': [52.3676, 51.9225, 52.0907, 52.0705, 53.2194, 51.9843, 50.8483, 52.9959, 53.2014, 52.3874],
        'lon': [4.9041, 4.4792, 5.1214, 4.3007, 6.5665, 5.8987, 5.6889, 6.5622, 5.8086, 4.6387],
        'province': ['North Holland', 'South Holland', 'Utrecht', 'South Holland', 'Groningen', 'Gelderland', 'Limburg',
                     'Drenthe', 'Friesland', 'North Holland'],
        'type': ['country', 'province', 'province', 'province', 'province', 'province', 'province', 'province',
                 'province', 'province']
    })

    province_capitals = folium.FeatureGroup(name='Province Capitals')
    main_capital = folium.FeatureGroup(name='Country Capital')

    for _, row in capitals_df.iterrows():
        if row['type'] == 'province':
            icon_color = 'red'
            layer = province_capitals
        else:
            icon_color = 'blue'
            layer = main_capital

        folium.Marker(
            location=[row['lat'], row['lon']],
            tooltip=row['city'],
            icon=folium.Icon(color=icon_color, prefix='fa', icon='star' if row['type'] == 'country' else 'circle')
        ).add_to(layer)

    province_capitals.add_to(netherlands_map)
    main_capital.add_to(netherlands_map)

    # add a layer control with a legend that is always visible
    folium.LayerControl(position='topleft', collapsed=False).add_to(netherlands_map)

    # display the map
    # display(HTML(netherlands_map._repr_html_()))
    return netherlands_map._repr_html_()

folium_html = demo_folium_map()
with open(r'webslides/modules/folium_demo.html', 'w') as f:
    f.write(folium_html)
print('folium_demo.html saved to file')