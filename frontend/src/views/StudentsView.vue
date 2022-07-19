<template>
  <v-card color="blue lighten-2" max-width="900"
    class="mx-auto" v-if="items.length>0">
      <v-card-title>
        Estudiantes
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Buscar estudiante"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="items"
        :search="search"
      >
      <template v-slot:[`item.actions`]="{item}">
        <v-btn
          small
          class="blue lighten-2"
          @click="seguir(item)"
        >
          Seleccionar
        </v-btn>
      </template>
      </v-data-table>
    </v-card>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
    name:'App',
    computed: {
        ...mapGetters(['user'])
    },
    data () {
        return {
            items:[],
            search: '',
            headers: [
                {
                text: 'Nombres',
                align: 'start',
                value: 'nombres',
                },
                { text: 'Apellido Paterno', value: 'paterno' },
                { text: 'Apellido Materno', value: 'materno' },
                { text: 'Rut', value: 'rut' },
                { text: 'Acciones', value: 'actions', sortable: false },
            ], 
        }
    },
    methods:{
        getData: async function(){
            if (this.user==null)
                this.$router.push('/');
            try {
                const response = await this.$http.get('/estudiantes');
                this.items = response.data     
            } catch (error) {
                console.log('error', error);
            }
        },
        seguir(item) {        
            const alumnoID = item.id;
            this.$router.push({name:'Estudiante',params:{id:alumnoID}});
        },
    },
    created:function(){
        this.getData();
    }
}
</script>