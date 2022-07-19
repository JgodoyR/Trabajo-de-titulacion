import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import './axios'
import store from './vuex'
import VueCookies from 'vue-cookies'
import VueMoment from 'vue-moment'
import moment from 'moment-timezone'
import 'moment/locale/es'
import Quill from 'quill'

Vue.config.productionTip = false
Vue.use(VueCookies);
Vue.$cookies.config({httpOnly:true})
Vue.use(VueMoment,{moment,})
moment.locale('es')

new Vue({
  vuetify,
  router,
  store,
  Quill,
  render: h => h(App)
}).$mount('#app')
