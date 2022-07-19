<template>
  <div id="app">

    <HeaderPage />

  </div>
</template>


<script>
//import axios from 'axios'
import HeaderPage from './components/HeaderPage.vue'

export default {

  name: 'App',
  components: {HeaderPage},
  /*async created(){
    const response = await axios.get('user');
    this.$store.dispatch('user', response.data);
  }*/

}

</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Fira+Sans:400,500,600,700,800');

  *{
    box-sizing: border-box;
  }

  body {
    background: #1C8EF9 !important;
    min-height: 100vh;
    display: flex;
    font-weight: 400;
    font-family: 'Fira Sans', sans-serif;
  }

  h1, h2, h3, h4, h5, h6, label, span {
    font-weight: 500;
    font-family: 'Fira Sans', sans-serif;
  }

  body, html, #app, #root, .auth-wrapper {
    width: 100%;
    height: 100%;
  }

  #app {
    text-align: center;
  }

  .navbar-light {
    background-color: #ffffff;
    box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
  }

  .auth-wrapper {
    display: flex;
    justify-content: center;
    flex-direction: column;
    text-align: left;
  }

  .auth-inner {
    width: 450px;
    margin: auto;
    background: #ffffff;
    box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
    padding: 40px 55px 45px 55px;
    border-radius: 15px;
    transition: all .3s;
  }

  .auth-wrapper .form-control:focus {
    border-color: #167bff;
    box-shadow: none;
  }

  .auth-wrapper h3 {
    text-align: center;
    margin: 0;
    line-height: 1;
    padding-bottom: 20px;
  }

  .custom-control-label {
    font-weight: 400;
  }

  .forgot-password,
  .forgot-password a {
    text-align: right;
    font-size: 13px;
    padding-top: 10px;
    color: #7f7d7d;
    margin: 0;
  }

  .forgot-password a {
    color: #167bff;
  }


</style>







<!--<template>
  <div id="app">
    <nav>
      <a href="https://informatica.usach.cl/" class="navbar-brand"> 
          <img src="https://informatica.usach.cl/wp-content/uploads/2021/05/cropped-logo_diinf_usach.png" width="25%" alt="Logo Diinf">
      </a>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </div>
</template>-->
<!--
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>-->
