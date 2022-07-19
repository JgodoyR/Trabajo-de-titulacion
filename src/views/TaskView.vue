<template>
    <v-container class="mt-2">
        <v-row justify="center">
            <v-col class="mr-2">
                <v-card width="450px" height="680px" class="text-center pa-md-2 mx-lg-auto">
                    <div v-if="items.tecnologia == 1">
                        <img width="105px" height="90px" src="./../assets/docker.png" alt="">
                    </div>
                    <div v-if="items.tecnologia == 2">
                        <img width="85px" height="90px" src="./../assets/git-logo.png" alt="">
                    </div>
                    <div v-if="items.tecnologia == 3">
                        <img width="205px" height="90px" src="./../assets/minikube-logo.png" alt="">
                    </div>
                    <h2 class="intro-text">{{ items.nombre }}</h2>
                    <br>
                    <div v-html="items.enunciado"></div>
                    <br><br>
                    <v-text-field
                    label="Ingrese su respuesta"
                    v-model="respuesta"
                    :counter="50"
                    required
                    outlined
                    dense
                    ></v-text-field>
                    <v-spacer></v-spacer>
                            
                    <v-spacer></v-spacer>

                    <v-btn
                        class="mr-4 mt-16"                                
                        color="success"
                        @click="()=>{enviar();stop();}"
                    >
                        Enviar respuesta
                    </v-btn>
                    <v-dialog
                        v-model="dialog"
                        max-width="290"
                        >
                        <v-card>
                            <v-card-title class="text-h5">
                            Respuesta enviada
                            </v-card-title>

                            <v-card-text>
                            Su respuesta ha sido enviada exitosamente.
                            </v-card-text>

                            <v-card-actions>

                            <v-spacer></v-spacer>

                            <v-btn
                                color="green darken-1"
                                text
                                @click="cerrar"
                            >   
                                Aceptar
                            </v-btn>

                        </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-card>
            </v-col>
            <v-col>
                <terminal-comp></terminal-comp>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import TerminalComp from '../components/TerminalComp.vue'
import {mapGetters} from 'vuex'

export default {

    name: 'App',
    components: { TerminalComp },
    computed: {
        ...mapGetters(['user']),
        formattedElapsedTime() {
            const date = new Date(null);
            date.setSeconds(this.elapsedTime / 1000);
            const utc = date.toUTCString();
            return utc.substr(utc.indexOf(":") - 2, 8);
        }
    },
    data () {
        return {
            items: [],
            items2: [],
            respuesta: '',
            estado: 0,
            dialog: false,
            elapsedTime: 1000,
            timer: undefined
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
                
                var result2 = await this.$http.get('/usuario_ejercicio/all');
                let response2 = result2.data;
                this.items2 = response2;      
                    
            } catch (error) {
                console.log('error', error);
            }
        },
        enviar: async function(){
            try{
                for(var k = 0; k < this.items2.length; k++){
                    if(this.items2[k].ejercicio == this.items.id && this.items2[k].usuario == this.user.id){
                        var result;
                        result = await this.$http.put('/usuario_ejercicio/'+this.items2[k].id,{
                            tiempo: this.elapsedTime,
                            respuesta: this.respuesta,
                            estado: 1,
                            ejercicio: this.items.id,
                            usuario: this.user.id
                        });
                        this.dialog = true;
                        this.respuesta = result.data;
                    }
                }
            }
            catch (error) {
                console.log('error', error);
            }
        },
        cerrar(){
          this.dialog = false;
          this.$router.push({name:'Tecnologias Ejercicios'});    
        },
        start() {
            this.elapsedTime = 1000;
            this.timer = setInterval(() => {
                this.elapsedTime += 1000;
            }, 1000);
        },
        stop() {
            clearInterval(this.timer);
        }
    },
    beforeMount() {
        this.start()
    },
    created:function(){
        this.getData();
    }

}
</script>

<style scoped>
h2.intro-text{
    font-size: 35px;
    font-weight: bold;
    color: rgb(0, 0, 0);
}
h3.instructions{
    font-size: 28px;
    font-weight: bold;
    color: rgb(6, 30, 247);
}
</style>