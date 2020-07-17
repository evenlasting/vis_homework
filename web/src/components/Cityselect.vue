<template>
<div>
  <el-checkbox-button :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全选</el-checkbox-button>
  <div style="margin: 15px 0;"></div>
  <el-checkbox-group v-model="checkedCities" @change="handleCheckedCitiesChange">
    <el-checkbox-button v-for="city in cities" :label="city" :key="city">{{city}}</el-checkbox-button>
  </el-checkbox-group>
</div>
</template>

<script>
  const cityOptions = ['Alabama', 'Alaska','Arizona', 'Arkansas', 'California', 'Colorado',
    'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 
    'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
    'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
    'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 
    'Pennsylvania', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Connecticut', 'Guam', 'Utah', 
    'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'Northern Mariana Islands', 'Rhode Island', 'West Virginia',
    'Wisconsin', 'Wyoming', 'Puerto Rico'];
  export default {
    data() {
      return {
        checkAll: false,
        checkedCities: ['Alabama', 'Alaska','Arizona', 'Arkansas', 'California', 'Colorado',
    'Delaware'],
        cities: cityOptions,
        isIndeterminate: true
      };
    },
    methods: {
      handleCheckAllChange(val) {
        this.checkedCities = val ? cityOptions : [];
        this.isIndeterminate = false;
        this.$emit("cityChange",this.checkedCities);
      },
      handleCheckedCitiesChange(value) {
        let checkedCount = value.length;
        this.checkAll = checkedCount === this.cities.length;
        this.isIndeterminate = checkedCount > 0 && checkedCount < this.cities.length;
        this.$emit("cityChange",this.checkedCities);
      }
    }
  };
</script>

<style>
.el-checkbox__input.is-checked+.el-checkbox__label{
  color:#FFFFFF !important;
  border-left:0px !important;
  border-radius:0px !important;
  border:0px !important;

}
.el-checkbox__label{
  color:#222222;
  border-left:0px;
  border-radius:0px;
  border:0px
}
.el-checkbox-button__inner{
  box-shadow: 0px 0px !important;
  border-left:0px !important;
  border-radius:0px !important;
  border:0px !important;
  background:#000 !important
}
</style>