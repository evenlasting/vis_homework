<template>
  <div id="Map"></div>
</template>

<script>
import mapboxgl from 'mapbox-gl';

export default {
  name: 'Map',
  props: {
  },
  mounted(){
    // mapboxgl.accessToken = 'pk.eyJ1Ijoia3dhbGtlcnRjdSIsImEiOiJMRk9JSmRvIn0.l1y2jHZ6IARHM_rA1-X45A';
    // const map = new mapboxgl.Map({
    // container: 'Map',
    // style: 'mapbox://styles/kwalkertcu/cizbggjq6006w2rnqzkmf6i0k', // stylesheet location
    // center: [-122.447303, 37.753574], // starting position [lng, lat]
    // zoom: 9 ,// starting zoom,
    // hash:true
    // });
    mapboxgl.accessToken = 'pk.eyJ1IjoiZXZlbmxhc3RpbmciLCJhIjoiY2tjbHhvMnh3MDk1NDJ5bGo2amN0a3RxYSJ9._0aKqW2jedZkRCmXXIi1SQ';
    var map = new mapboxgl.Map({
    container: 'Map',
    style: 'mapbox://styles/mapbox/dark-v10', // stylesheet location
    // center: [-95, 40], // starting position [lng, lat]
    // zoom: 3 // starting zoom
    center: [-79.999732, 40.4374], 
    zoom: 11
    });
    map.on('load',function(){
      map.addSource('trees',{
        type: 'geojson',
      data: './trees.geojson'
      });
      map.addLayer({
        id: 'trees-heat',
        type: 'heatmap',
        source: 'trees',
        maxzoom: 15,
        paint: {
        // increase weight as diameter breast height increases
        'heatmap-weight': {
        property: 'dbh',
        type: 'exponential',
        stops: [
        [1, 0],
        [62, 1]
        ]
        },
        // increase intensity as zoom level increases
        'heatmap-intensity': {
        stops: [
        [11, 1],
        [15, 3]
        ]
        },
        // assign color values be applied to points depending on their density
        'heatmap-color': [
        'interpolate',
        ['linear'],
        ['heatmap-density'],
        0, 'rgba(236,222,239,0)',
        0.2, 'rgb(208,209,230)',
        0.4, 'rgb(166,189,219)',
        0.6, 'rgb(103,169,207)',
        0.8, 'rgb(28,144,153)'
        ],
        // increase radius as zoom increases
        'heatmap-radius': {
        stops: [
        [11, 15],
        [15, 20]
        ]
        },
        // decrease opacity to transition into the circle layer
        'heatmap-opacity': {
        default: 1,
        stops: [
        [14, 1],
        [15, 0]
        ]
        },
        }
        }, 'waterway-label');
      
    })
  }
}
</script>

<style>
#Map {
  overflow:visible;
  height:700px
}
</style>