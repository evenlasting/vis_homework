<template>
  <div id="app">
    <div id="main" style="width: 400px;height:700px;"></div>
  </div>
</template>
<script>
export default {
  name: "app",
  watch:{
      timeDate:{
          handler(val,oldVal){
              console.log(val,oldVal,this.time)
              this.drawChart()
          },
          deep:true,
          immediate: true,
      },
      cities:{
          handler(val,oldVal){
              console.log(val,oldVal)
              console.log(this.time)
              this.drawChart()
          },
          deep:true
      }
  },
  props:{
    time:{
      default:new Date(2020,6,7)
    },
    timeDate:{
        default:(new Date(2020,6,7)).getDate()
    },
    cities:{
      default:['Alabama']
    }
  },
  methods: {
    drawChart() {
      // 基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.getElementById("main"));
      // 指定图表的配置项和数据
      let url='http://127.0.0.1:5000/api/tree?cities='
      let citiesUrl=this.cities.join(',')
      let timeUrl='&d='+String(this.time.getDate())+'&m='+String(this.time.getMonth()+1)+'&y='+String(this.time.getFullYear())
      url=url+citiesUrl+timeUrl
      this.$axios.get(url).then(diskData => {
        diskData=diskData.data

        var formatUtil = this.$echarts.format;


        myChart.setOption({

            title: {
                text: 'Disk Usage',
                left: 'center'
            },

            tooltip: {
                formatter: function (info) {
                    var value = info.value;
                    var treePathInfo = info.treePathInfo;
                    var treePath = [];

                    for (var i = 1; i < treePathInfo.length; i++) {
                        treePath.push(treePathInfo[i].name);
                    }

                    return [
                        '<div class="tooltip-title">' + formatUtil.encodeHTML(treePath.join('/')) + '</div>',
                        'Disk Usage: ' + formatUtil.addCommas(value) + ' KB',
                    ].join('');
                }
            },

            series: [
                {
                    name: 'Disk Usage',
                    type: 'treemap',
                    visibleMin: 300,
                    label: {
                        show: true,
                        formatter: '{b}'
                    },
                    upperLabel: {
                        show: true,
                        height: 30
                    },
                    itemStyle: {
                        borderColor: '#fff'
                    },
                    levels: [
                {
                    itemStyle: {
                        borderColor: '#777',
                        borderWidth: 0,
                        gapWidth: 1
                    },
                    upperLabel: {
                        show: false
                    }
                },
                {
                    itemStyle: {
                        borderColor: '#555',
                        borderWidth: 5,
                        gapWidth: 1
                    },
                    emphasis: {
                        itemStyle: {
                            borderColor: '#ddd'
                        }
                    }
                },
                {
                    colorSaturation: [0.35, 0.5],
                    itemStyle: {
                        borderWidth: 5,
                        gapWidth: 1,
                        borderColorSaturation: 0.6
                    }
                }
            ],
                    data: diskData
                }
            ]
        });
      })
    }
  },
  mounted() {
    this.drawChart();
  }
};
</script>