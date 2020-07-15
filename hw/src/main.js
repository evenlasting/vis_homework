import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import '../index.css';
import echarts from 'echarts'
import axios from 'axios'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.$echarts=echarts
Vue.prototype.$axios=axios

new Vue({
  render: h => h(App),
}).$mount('#app')
