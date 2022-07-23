//import axios from 'axios'
//axios.defaults.baseURL = 'http://localhost:8000';

import axios from 'axios'
import Vue from 'vue'

const axiosInstance = axios.create({ 
  baseURL: 'http://198.199.82.240:8000'
})

Vue.prototype.$http = axiosInstance;

axios.defaults.headers.common['Authorization'] = 'Bearer' + localStorage.getItem('token');

