<template>
  <v-card color="blue darken-3" max-width="900"
    class="mx-auto">
    <v-card-title class="text-center justify-center py-6">
      <h1 class="font-weight-bold text-h5 white--text">
        Progreso de {{ items.nombres }} {{ items.paterno }} {{ items.materno }}
      </h1>
    </v-card-title>
    
    <v-simple-table >
      <template v-slot:default>
        <thead>
          <br>
          <h3>Cantidad de ejercicios resueltos: {{ cant_ejercicios_resueltos }} de {{ cant_ejercicios }} </h3>
          <h3>Cantidad de clases completadas: {{ cant_clases_completadas }} de {{ cant_clases }} </h3>
          <h3>Tiempo total dedicado: {{ formattedElapsedTime(tiempo_ejercicios + tiempo_clases) }} </h3>
          <h3>Último inicio de sesión: {{ items.last_login | moment("dddd, Do [de] MMMM [del] YYYY, h:mm:ss a") }}</h3>

          <br><br>
          
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>
                <strong>Clases</strong> 
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-data-table
                :headers="headers2"
                :items="items2"
                >
                  <template v-slot:[`item.estado`]="{ item }">
                    <div :class="getStyleEstado(item.estado)">{{ item.estado == 1 ? 'Completada' : 'No completada' }}</div>
                  </template>
                </v-data-table> 
              </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
              <v-expansion-panel-header>
                <strong>Ejercicios</strong> 
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-data-table
                :headers="headers3"
                :items="items3"
                >
                  <template v-slot:[`item.estado`]="{ item }">
                    <v-icon v-if="item.estado == 1" color="green">mdi-check-circle</v-icon>
                    <v-icon v-else color="grey">mdi-check-circle</v-icon>
                  </template>
                  <template v-slot:[`item.tiempo`]="{ item }">
                    <div :class="formattedElapsedTime(item.tiempo)">{{ item.tiempo != null ? formattedElapsedTime(item.tiempo) : ' ' }}</div>
                  </template>
                  
          
                  <template v-slot:[`item.respuesta`]="{ item }">
                    <v-icon v-if="item.estado == 0" color="grey">mdi-help-circle-outline</v-icon>
                    <v-icon v-else-if="item.respuesta == item.ejercicio.respuesta1" color="green">mdi-check-circle</v-icon>
                    <v-icon v-else-if="item.respuesta == item.ejercicio.respuesta2" color="green">mdi-check-circle</v-icon>
                    <v-icon v-else color="red">mdi-close-circle-outline</v-icon>
                  </template>

                </v-data-table>            
              </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
              <v-expansion-panel-header>
                <strong>Calendario</strong> 
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <div>
                  <v-sheet
                    tile
                    height="54"
                    class="d-flex justify-center"
                  >
                    <v-btn
                      icon
                      class="ma-2"
                      @click="$refs.calendar.prev()"
                    >
                      <v-icon>mdi-chevron-left</v-icon>
                    </v-btn>
                    <v-toolbar-title class="pt-3" v-if="$refs.calendar">
                          {{ $refs.calendar.title }}
                    </v-toolbar-title>
                    <v-btn
                      icon
                      class="ma-2"
                      @click="$refs.calendar.next()"
                    >
                      <v-icon>mdi-chevron-right</v-icon>
                    </v-btn>
                  </v-sheet>
                  <div class="d-flex justify-center">
                    <v-sheet class="d-flex" height="340" width="300">
                    <v-calendar
                      ref="calendar"
                      v-model="value"
                      :events="events"
                      :event-overlap-threshold="30"
                      :event-color="getEventColor"
                      @change="getEvents"
                    ></v-calendar>
                  </v-sheet>
                  </div>
                  
                </div>

              </v-expansion-panel-content>
            </v-expansion-panel>

          </v-expansion-panels>
          
        </thead>
      
      </template>
    </v-simple-table>
  </v-card>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
    computed: {
        ...mapGetters(['user']),
    },
    data () {
        return {
            cant_ejercicios_resueltos: null,
            cant_clases_completadas: null,
            cant_ejercicios: null,
            cant_clases: null,
            tiempo_ejercicios: null,
            tiempo_clases: null,
            tiempo_dedicado: null,
            ejercicios: [],
            items: [],
            items2: [],
            items3: [],
            headers2: [
                {
                text: 'Nombre de la clase',
                align: 'start',
                value: 'clase.titulo',
                },
                { text: 'Estado', value: 'estado'},
            ], 
            headers3: [
                {
                text: 'Nombre del ejercicio',
                align: 'start',
                value: 'ejercicio.nombre',
                },
                { text: 'Tiempo', value: 'tiempo'},
                { text: 'Estado', value: 'estado'},
                { text: 'Respuesta', value: 'respuesta'}
            ], 

            type: 'month',
            mode: 'stack',
            value: '',
            events: [],
            colors: ['green'],
            names: ['x'],
        }
    },
    methods:{
        getData: async function(){
            if (this.user==null)
                this.$router.push('/');
            try {
                let response = await this.$http.get(this.$route.path);
                this.items  = response.data;

                let response2 = await this.$http.get('/clase_usuario/'+this.items.id);
                this.items2 = response2.data;

                let response3 = await this.$http.get('/ejercicio_usuario/'+this.items.id);
                this.items3 = response3.data;

                let response4 = await this.$http.get('/contar_ejercicios_resueltos/'+this.items.id);
                this.cant_ejercicios_resueltos = response4.data;

                let response5 = await this.$http.get('/contar_clases_completadas/'+this.items.id);
                this.cant_clases_completadas = response5.data;

                let response6 = await this.$http.get('/sumar_tiempo_ejercicios/'+this.items.id);
                this.tiempo_ejercicios = response6.data;

                let response7 = await this.$http.get('/sumar_tiempo_clases/'+this.items.id);
                this.tiempo_clases = response7.data;

                let response8 = await this.$http.get('/contar_ejercicios');
                this.cant_ejercicios = response8.data;

                let response9 = await this.$http.get('/contar_clases');
                this.cant_clases = response9.data;

            } catch (error) {
                console.log('error', error);
            }
        },
        getStyleEstado(estado){
          if(estado == 0)
            return 'red--text font-weight-bold'
          else
            return 'green--text font-weight-bold'
        },
        formattedElapsedTime(tiempo) {
            const date = new Date(null);
            date.setSeconds(tiempo / 1000);
            const utc = date.toUTCString();
            return utc.substr(utc.indexOf(":") - 2, 8);
        },
        getDate(datetime){
          let date = new Date(datetime);
          return date;
        },
        getEvents (){
          const events = []

          events.push({
            name: this.names[0],
            start: this.getDate(this.items.last_login),
            color: this.colors[0]
          })

          this.events = events
        },
        getEventColor (event) {
          return event.color
        },
    },
    created:function(){
        this.getData();
    },
    beforeMount() {
        this.getEvents();
        this.getEventColor(event);
    },
}
</script>
