<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      v-if="user"
    >
      <v-list dense>

        <router-link to="/">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-home</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Inicio</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>

        <router-link v-if="user.rol==1 || user.rol==2" to="/agregar-tecnologia">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-database-plus-outline</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Agregar tecnologia</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link> 

        <router-link v-if="user.rol==1 || user.rol==2" to="/crear-clase">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-note-plus-outline</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Crear una clase</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link> 

        <router-link v-if="user.rol==1 || user.rol==2" to="/crear-ejercicio">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-pencil-plus-outline</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Crear un ejercicio</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>   

        <router-link v-if="user.rol==1 || user.rol==2" to="/alumnos">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-account-details-outline</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Estudiantes</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>   

        <router-link v-if="user.rol==1 || user.rol==3" to="/tecnologias-clases">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-notebook-multiple</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Clases</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>   

        <router-link v-if="user.rol==1 || user.rol==3" to="/tecnologias-ejercicios">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-pencil-outline</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Ejercicios</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>   

        <router-link v-if="user.rol==1 || user.rol==3" to="/playground">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-application-brackets</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Playgrounds</v-list-item-title>
            </v-list-item-content>
          </v-list-item>            
        </router-link>   

        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

        <v-list-item link>
          <v-list-item-content>
            <v-btn title="Cerrar sesión" class="red" color="white" text small @click="cerrar" >
              Cerrar sesión 
            </v-btn>
          </v-list-item-content>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="blue lighten-4"
      dark
      height="120"
      v-if="user"
    >
      <v-app-bar-nav-icon  @click.stop="drawer = !drawer"></v-app-bar-nav-icon>      
      
      <img src="https://informatica.usach.cl/wp-content/uploads/2021/05/cropped-logo_diinf_usach.png" style="float: right; margin: 5 0 1em 2em" alt="Logo de usach" width="380" height="110">
      <v-toolbar-title style="margin-left:30px;">
        Aplicación web orientada a la enseñanza y aprendizaje de tecnologías de Despliegue Continuo de DevOps
      </v-toolbar-title>
    </v-app-bar>

    <nav class="navbar navbar-expand navbar-light fixed-top" v-if="!user">
       <div class="">
        
      <a href="https://informatica.usach.cl/" class="navbar-brand"> 
        <img src="https://informatica.usach.cl/wp-content/uploads/2021/05/cropped-logo_diinf_usach.png" alt="Logo Diinf">
      </a>
    </div>
      <div class="container">
        <div class="collapse navbar-collapse">


          <ul class="navbar-nav ml-auto" v-if="!user">
            <li class="nav-item" >
              <router-link to="/login" class="nav-link">Iniciar sesión </router-link>
            </li>
    
          </ul>

          <ul class="navbar-nav ml-auto" v-if="user">
            <li class="nav-item" >
              <a href="https://informatica.usach.cl/" @click="handleClick" class="nav-link">Cerrar sesion</a>
            </li>
            <li class="nav-item" >
              <router-link to="/" class="nav-link">inicio</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <v-main>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          justify="center"
        >
          <v-col class="text-center">            
              <router-view/>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>    

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'App',
  computed: {
      ...mapGetters(['user'])
  },
  data(){
        return{
            drawer: null,
            actual:null,
            cosas: null,   
            test: false,  
        }
    },
      
  methods: {
      getData: async function(){
            try {
                this.cosas = this.$cookies.get("token");
                if(this.user==null && this.cosas!=null)
                {
                  var result2 = await this.$http.post('/user', { jwt: this.cosas.jwt});
                  let response2 = result2.data; 
                  this.$store.dispatch('user', response2);
                }
                
            } catch (error) {
                console.log('error', error);
            }
      },
      cerrar() {
        this.$store.dispatch('user',null);
        this.$cookies.remove("token");
        this.cosas=[];
        this.$router.push('/');
      },

    },
    created:function(){
        this.getData();
    },
    
  props: {
      source: String,
    }
    
};
</script>