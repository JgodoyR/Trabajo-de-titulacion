<template>
  <div v-if="count>0">
    <v-card
      color="blue darken-3" max-width="900"
      class="mx-auto"
    >
    
      <v-container>
        <v-row 
          v-for="(item2, i) in items2"
          :key="i"
          dense>
          <v-col
            
            cols="12"
          >
                <v-card color="white">
                  <div class="justify-space-between">
                    <div>
                      <v-card-title class="text-h6 justify-center">{{item2.ejercicio.nombre}} </v-card-title>
                      <v-card-subtitle v-html="item2.ejercicio.enunciado"></v-card-subtitle>
                      <v-card-actions>
                        <v-btn
                          class="mx-auto my-5"
                          color="blue darken-1"
                          outlined
                          rounded
                          small
                          @click="goToTask(item2)"
                        >
                          Ir al ejercicio
                        </v-btn>
                      </v-card-actions>
                    </div>
                  </div>
                </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </div>

  <div v-else>
    <v-card
      class="mx-auto my-12"
      color="#29B6F6"
      max-width="900"
      elevation="15"
    >
      <v-card-title class="mx-auto justify-center">No hay ejercicios para realizar</v-card-title>
    </v-card>
  </div>
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
            items:[],
            items2:[],
            count: 0
        }
    },
    methods:{
        getData: async function(){
            if (this.user==null)
            this.$router.push('/');
            try {
                var result = await this.$http.get(this.$route.path);
                let response = result.data;
                this.items = response; 
                
                var result2 = await this.$http.get('listar_ejercicios_usuario_tecnologia/'+this.items.id+'/'+this.user.id);
                let response2 = result2.data;
                this.items2 = response2;

                for(var k = 0; k < this.items2.length; k++){
                  if(this.items2[k].ejercicio.tecnologia == this.items.id){
                    this.count++;
                  }
                }

            } catch (error) {
                console.log('error', error);
            }
        },
        goToTask(item) {
            const ejercicioID = item.ejercicio.id;
            this.$router.push({name:'Ejercicio',params:{id:ejercicioID}});
        },
    },
    created:function(){
        this.getData();
    }
}
</script>

<!--<template>
    <v-container class="mt-n16">
        <h1>Ejercita las distintas tecnologías de Despliegue Continuo</h1>
        <v-container class="mt-10">
            <v-row justify="center">
                <v-col class="mr-10"> 
                    <v-card class="text-center pa-md-4 mx-lg-auto">
                        <router-link to="/ejercicios-docker">
                            <img width="280px" height="250px" src="./../assets/docker.png" alt="">
                        </router-link>
                    </v-card>
                </v-col>
                <v-col class="mr-10"> 
                    <v-card class="text-center pa-md-4 mx-lg-auto">
                        <router-link to="/ejercicios-git">
                            <img width="250px" height="250px" src="./../assets/git-logo.png" alt="">
                        </router-link>
                    </v-card>
                </v-col>
                <v-col > 
                    <v-card class="text-center pa-md-4 mx-lg-auto">
                        <router-link to="/ejercicios-minikube">
                            <img width="490px" height="250px" src="./../assets/minikube-logo.png" alt="">
                        </router-link>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-container>
</template>

<script>
import {mapGetters} from 'vuex'

export default {

    name: 'App',
    computed: {
        ...mapGetters(['user'])
    }
}
</script>-->