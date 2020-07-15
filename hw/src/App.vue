<template>
  <div id="app">
    <el-row>
      <el-col :span="4">
        <div class="grid-head bg-dark">
        <Timeselect/>
        </div>
        <div class="grid-foot bg-purple-dark">
        <Cityselect/>
        </div>
      </el-col>
      <el-col :span="16">
        <div class="grid-content bg-purple-light">
          <Map/>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple">
        <Tree/>
        </div>
      </el-col>
    </el-row>


  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Map from './components/Map.vue'
import Timeselect from './components/Timeselect.vue'
import Cityselect from './components/Cityselect.vue'
import Tree from
 './components/Tree.vue'

export default {
  name: 'App',
  components: {
    //HelloWorld
    Timeselect,
    Map,
    Cityselect,
    Tree
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
   border-radius: 0px
}
.bg-purple-dark {
  background: #000000;
}
.bg-purple {
  background: #000000;
}
.bg-dark{
  background: #000000;
}
.bg-purple-light {
  background: #000000;
}
.grid-content {
  border-radius: 0px;
  min-height: 700px;
}
.grid-foot{
  border-radius: 0px;
  min-height: 660px;
}
.grid-head{
  padding-top:20px;
  border-radius: 0px;
  padding-bottom: 100px
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
