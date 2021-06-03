import folium
from django.shortcuts import render,redirect
from . import map_fun as mf


def showmap(request):
    return render(request,'mp.html')

def dummyfun(request,lat1,long1):
    figure = folium.Figure()
    long2,lat2=79.7678,11.7149
    lat1=float(lat1)
    long1=float(long1)
    
    route=mf.get_route(long1,lat1,long2,lat2)
    m = folium.Map(location=[(route['start_point'][0] + route['end_point'][0])/2, 
                                 (route['start_point'][1] + route['end_point'][1])/2], 
                       zoom_start=13)
    m.add_to(figure)
        

    folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)

    folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)

    folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
    figure.render()
    context={'map':figure}
    return render(request,'map.html',context)
