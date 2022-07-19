<template>
  <v-card
    color="blue darken-3" max-width="900"
    class="mx-auto"
  >

    <v-container>
      <v-row dense>
        <v-col
          v-for="(item1, i) in items1"
          :key="i"
          cols="12"
        >
          <div v-if="item1.estado == 0">
            <v-card
            color="white"
            >
              <div class="justify-space-between">
                <div>
                  <v-card-title
                    class="text-h6 justify-center"                  
                  >Clase: {{item1.clase.titulo}} </v-card-title>

                  <v-card-subtitle v-html="item1.clase.descripcion"></v-card-subtitle>

                  <v-card-actions>

                    <v-btn
                      class="mx-auto my-5"
                      color="blue darken-1"
                      outlined
                      rounded
                      small
                      @click="goToClass(item1)"
                    >
                      Ir a la clase
                    </v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>
          </div>
          <div v-else>
            <v-card
            color="green lighten-3"
            >
              <div class="justify-space-between">
                <div>
                  <v-card-title
                    class="text-h6 justify-center"                  
                  >Clase: {{item1.clase.titulo}} </v-card-title>

                  <v-card-subtitle v-html="item1.clase.descripcion"></v-card-subtitle>

                  <v-card-actions>

                    <v-btn
                      class="mx-auto my-5"
                      color="blue darken-1"
                      outlined
                      rounded
                      small
                      @click="goToClass(item1)"
                    >
                      Ir a la clase
                    </v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>
          </div>
          
   

        </v-col>
      </v-row>
    </v-container>
  </v-card>
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
            items1:[],
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

                var result1 = await this.$http.get('/listar_clases_usuario_tecnologia/'+this.items.id+'/'+this.user.id);
                let response1 = result1.data;
                this.items1 = response1;

            } catch (error) {
                console.log('error', error);
            }
        },
        goToClass(item) {
            const claseID = item.clase.id;
            this.$router.push({name:'Clase',params:{id:claseID}});
        },
    },
    created:function(){
        this.getData();
    },
}
</script>