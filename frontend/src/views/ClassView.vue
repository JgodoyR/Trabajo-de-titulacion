<template>
    <v-container class="mt-2">
        <v-row justify="center">
            <v-col class="mr-2">
                <v-card width="450px" height="680px" class="text-center pa-md-4 mx-lg-auto">
                    <div v-if="items.tecnologia == 1">
                        <img width="105px" height="90px" src="./../assets/docker.png" alt="">
                    </div>
                    <div v-if="items.tecnologia == 2">
                        <img width="85px" height="90px" src="./../assets/git-logo.png" alt="">
                    </div>
                    <div v-if="items.tecnologia == 3">
                        <img width="205px" height="90px" src="./../assets/minikube-logo.png" alt="">
                    </div>
                    <h2 class="intro-text">{{ items.titulo }}</h2>
                    <br>
                    <div v-html="items.descripcion"></div>
                    <br><br><br><br>
                    <v-btn
                        class="mr-4"                                
                        color="success"
                        @click="()=>{enviar();cerrar();}"
                    >
                        Terminar
                    </v-btn>
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
        ...mapGetters(['user'])
    },
    data () {
        return {
            items: [],
            items2: [],
            elapsedTime: 1000,
            //claseID: null,
        }
    },
    watch:{
        id: function(){
            this.getData()
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

                var result2 = await this.$http.get('/usuario_clase/all');
                let response2 = result2.data;
                this.items2 = response2;  
                
            } catch (error) {
                console.log('error', error);
            }
        },
        enviar: async function(){
            try{
                for(var k = 0; k < this.items2.length; k++){
                    if(this.items2[k].clase == this.items.id && this.items2[k].usuario == this.user.id && this.items2[k].estado == 0){
                        var result;
                        result = await this.$http.put('/usuario_clase/'+this.items2[k].id,{
                            estado: 1,
                            clase: this.items.id,
                            usuario: this.user.id, 
                            tiempo: this.elapsedTime
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
        cambiarEstado: async function(){
            try{
                for(var k = 0; k < this.items2.length; k++){
                    if(this.items2[k].clase == this.items.id && this.items2[k].usuario == this.user.id){
                        var result;
                        result = await this.$http.put('/usuario_clase/'+this.items2[k].id,{
                            estado: 1,
                            clase: this.items.id,
                            usuario: this.user.id, 
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
        start() {
            this.elapsedTime = 1000;
            this.timer = setInterval(() => {
                this.elapsedTime += 1000;
            }, 1000);
        },
        cerrar(){
          clearInterval(this.timer);  
          this.$router.push({name:'Tecnologias Clases'});    
        },
        /*siguiente(){
            clearInterval(this.timer);  
            try{
                for(var k = 0; k < this.items3.length; k++){
                    if(this.items3[k].id == this.items.id){
                        this.claseID = this.items3[k+1].id;
                    }
                }
            }
            catch (error) {
                console.log('error', error);
            }
            this.$router.go({name:'Clase Docker',params:{id:this.claseID}})
        }*/
    },
    created:function(){
        this.getData();
    },
    beforeMount() {
        this.cambiarEstado()
        this.start()
    },
    /*mounted(){
        //this.cambiarEstado()
    },
    beforeUnmount(){
        //this.cambiarEstado()
    },*/

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