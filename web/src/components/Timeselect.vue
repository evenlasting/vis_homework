<template>
  <div class="time">
    <el-button type="primary" class="left" icon="el-icon-caret-top" @click='minusDate'></el-button>
    <div class="demonstration">{{dateString}}</div>
    <el-button type="primary" class="right" icon="el-icon-caret-bottom" @click='addDate'></el-button>
  </div>
</template>

<script>

let today=new Date(2020,6,7)

export default {
  name: 'Timeselect',
  data(){
    return {
      // dateString:(today.getMonth()).toString()+"/"+(today.getDay()).toString()
      dateString:today.toDateString()
    }
  },
  methods:{
    minusDate:function(){
      today.setDate(today.getDate()-1)
      this.dateString=today.toDateString()
      this.$emit("timeChange",today)
    },
    addDate:function(){
      today.setDate(today.getDate()+1)
      this.dateString=today.toDateString()
      this.$emit("timeChange",today)
    }
  }
}
</script>

<style>
.left{
}
.right{
}
.el-input__inner{
  width:100%
}
.demonstration{
  color:#f1939c;
}
</style>