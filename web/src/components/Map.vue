<template>
  <div id="Map"></div>
</template>

<script>
import mapboxgl from 'mapbox-gl';

export default {
  name: 'Map',
  watch:{
      timeDate:{
          handler(val,oldVal){
              console.log(val,oldVal,this.time)
              this.updateMap()
          },
          deep:true,
          immediate: true,
      },
      cities:{
          handler(val,oldVal){
              console.log(val,oldVal)
              console.log(this.time)
              this.updateMap()
          },
          deep:true
      }
  },
  methods:{
    updateMap(){
      let map=this.map
      map.removeLayer('trees-heat')
      map.removeLayer('trees-point')
      map.removeSource('trees')
      let url='http://127.0.0.1:5000/api/map?cities='
      let citiesUrl=this.cities.join(',')
      let timeUrl='&d='+String(this.time.getDate())+'&m='+String(this.time.getMonth()+1)+'&y='+String(this.time.getFullYear())
      url=url+citiesUrl+timeUrl
      this.$axios.get(url).then(diskData => {
        diskData=diskData.data
        map.addSource('trees',{
        type: 'geojson',
        data: diskData
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
        [1000, 1]
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
          [1,5],
          [9,100]
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
      map.addLayer({
        id: 'trees-point',
        type: 'circle',
        source: 'trees',
        minzoom: 14,
        paint: {
        // increase the radius of the circle as the zoom level and dbh value increases
        'circle-radius': {
        property: 'dbh',
        type: 'exponential',
        stops: [
        [{zoom: 15, value: 1 }, 5],
        [{zoom: 15, value: 62 }, 10],
        [{zoom: 22, value: 1 }, 20],
        [{zoom: 22, value: 62 }, 50],
        ]
        },
        'circle-color': {
        property: 'dbh',
        type: 'exponential',
        stops: [
        [0, 'rgba(236,222,239,0)'],
        [10, 'rgb(236,222,239)'],
        [20, 'rgb(208,209,230)'],
        [30, 'rgb(166,189,219)'],
        [40, 'rgb(103,169,207)'],
        [50, 'rgb(28,144,153)'],
        [60, 'rgb(1,108,89)']
        ]
        },
        'circle-stroke-color': 'white',
        'circle-stroke-width': 1,
        'circle-opacity': {
        stops: [
        [14, 0],
        [15, 1]
        ]
        }
        }
        }, 'waterway-label')
    
      })
    }
  },
  props: {
    time:{
      default:new Date(2020,6,7)
    },
    timeDate:{
        default:(new Date(2020,6,7)).getDate()
    },
    cities:{
      default:[]
    }
  },
  mounted(){
    mapboxgl.accessToken = 'pk.eyJ1IjoiZXZlbmxhc3RpbmciLCJhIjoiY2tjbHhvMnh3MDk1NDJ5bGo2amN0a3RxYSJ9._0aKqW2jedZkRCmXXIi1SQ';
    var map = new mapboxgl.Map({
    container: 'Map',
    style: 'mapbox://styles/mapbox/dark-v10', // stylesheet location
    // center: [-95, 40], // starting position [lng, lat]
    // zoom: 3 // starting zoom
    center: [-79.999732, 40.4374], 
    zoom: 11
    });
    this.map=map
    map.on('load',function(){
      map.addSource('trees',{
        type: 'geojson',
        data: './test(1).geojson'
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
        [1000, 1]
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
          [1,5],
          [9,100]
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
      map.addLayer({
        id: 'trees-point',
        type: 'circle',
        source: 'trees',
        minzoom: 14,
        paint: {
        // increase the radius of the circle as the zoom level and dbh value increases
        'circle-radius': {
        property: 'dbh',
        type: 'exponential',
        stops: [
        [{zoom: 15, value: 1 }, 5],
        [{zoom: 15, value: 62 }, 10],
        [{zoom: 22, value: 1 }, 20],
        [{zoom: 22, value: 62 }, 50],
        ]
        },
        'circle-color': {
        property: 'dbh',
        type: 'exponential',
        stops: [
        [0, 'rgba(236,222,239,0)'],
        [10, 'rgb(236,222,239)'],
        [20, 'rgb(208,209,230)'],
        [30, 'rgb(166,189,219)'],
        [40, 'rgb(103,169,207)'],
        [50, 'rgb(28,144,153)'],
        [60, 'rgb(1,108,89)']
        ]
        },
        'circle-stroke-color': 'white',
        'circle-stroke-width': 1,
        'circle-opacity': {
        stops: [
        [14, 0],
        [15, 1]
        ]
        }
        }
        }, 'waterway-label')
    });
  }
}
</script>

<style>
#Map {
  overflow:visible;
  height:700px;
  z-index:0 !important;
  border:0px
}
.mapboxgl-canvas{
  z-index:0 !important;
}
</style>