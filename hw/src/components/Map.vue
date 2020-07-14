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
    center: [-74.5, 40], // starting position [lng, lat]
    zoom: 9 // starting zoom
    });
    console.log(map)
  }
}
</script>

<style>
#Map {
  overflow:visible;
  height:700px
}
</style>