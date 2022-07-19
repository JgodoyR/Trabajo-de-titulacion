<template>
    <div>
        <h1>Aprenda las distintas tecnologías de Despliegue Continuo</h1>
        <v-card
        color="blue darken-3" max-width="900"
        class="mx-auto"
        >   
        <v-container class="mt-10">
            <v-row justify="center">
                <v-col
                v-for="(item, i) in items"
                :key="i"
                cols="12"
                >
                    <v-card class="text-center pa-md-2 mx-lg-auto">
                        <div v-if="item.nombre == 'Docker'">
                                <img width="60px" height="60px" src="./../assets/docker.png" alt="">
                        </div>
                        <div v-if="item.nombre == 'Git'">
                                <img width="50px" height="50px" src="./../assets/git-logo.png" alt="">
                        </div>
                        <div v-if="item.nombre == 'Minikube'">
                                <img width="100px" height="50px" src="./../assets/minikube-logo.png" alt="">
                        </div>
                        <v-card-title class="text-h6 justify-center" >
                            {{item.nombre}}
                        </v-card-title>
                        <v-card-actions>
                            <v-btn
                            class="mx-auto my-1"
                            color="blue darken-1"
                            outlined
                            rounded
                            small
                            @click="goToClasses(item)"
                            >
                                Ir a las clases
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
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
            items: [],
        }
    },
    methods:{
        getData: async function(){
            if (this.user==null)
              this.$router.push('/');
            try {
                var result = await this.$http.get('/tecnologias/all');
                let response = result.data;
                this.items = response;

            } catch (error) {
                console.log('error', error);
            }
        },
        goToClasses(item) {
            const tecnologiaID = item.id;
            this.$router.push({name:'Clases',params:{id:tecnologiaID}});
        },
    },
    created:function(){
        this.getData();
    },
}
</script>