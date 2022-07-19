<template>
  <nav class="navbar navbar-expand navbar-light fixed-top">
       <div class="">
        
      <a href="https://informatica.usach.cl/" class="navbar-brand"> 
        <img src="https://informatica.usach.cl/wp-content/uploads/2021/05/cropped-logo_diinf_usach.png" alt="Logo Diinf">
      </a>
    </div>
      <div class="container">
        <div class="collapse navbar-collapse">


          <ul class="navbar-nav ml-auto" v-if="!user">
            <li class="nav-item" >
              <router-link to="/login" class="nav-link">Iniciar sesion</router-link>
            </li>
            <li class="nav-item" >
              <router-link to="/" class="nav-link">Inicio</router-link>
            </li>
          </ul>

          <ul class="navbar-nav ml-auto" v-if="user">
            <li class="nav-item" >
              <a href="https://informatica.usach.cl/" @click="handleClick" class="nav-link">Cerrar sesion</a>
            </li>
            <li class="nav-item" >
              <router-link to="/" class="nav-link">Inicio</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</template>

<script >
import {mapGetters} from 'vuex'

export default{
  name: 'NavPage',
  methods: {
    handleClick() {
      this.$store.dispatch('user',null);
      this.$router.push('/');
    }
  },
  computed: {
    ...mapGetters(['user'])
  }
}
</script>