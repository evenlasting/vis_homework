<template>
  <div id="app">
    <el-row>
      <el-col :span="4">
        <div class="grid-head bg-purple"></div>
        <div class="grid-foot bg-purple-dark"></div>
      </el-col>
      <el-col :span="16">
        <div class="grid-content bg-purple-light"></div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple"></div>
      </el-col>
    </el-row>


  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    //HelloWorld
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
  margin-top: 60px;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 700px;
}
.grid-foot{
  border-radius: 4px;
  min-height: 350px;
}
.grid-head{
  border-radius: 4px;
  min-height: 350px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
