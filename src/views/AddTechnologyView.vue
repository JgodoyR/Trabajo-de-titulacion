<template>
    <v-card color="blue darken-3" max-width="900" class="mx-auto">
        <v-container class="mt-5">
            <v-stepper v-model="e6" vertical>
                <v-stepper-step
                :complete="e6 > 1"
                step="1"
                >
                Agregar tecnologia
                </v-stepper-step>

                <v-stepper-content step="1">
                <v-card           
                    class="mb-12"
                >
                <v-card-title class="text-h6">
                Rellene los siguientes datos:
                </v-card-title>
                    <v-card-text class="white text--primary">
                        <validation-observer
                            ref="observer"
                            v-slot="{ invalid }"
                        >
                            <form @submit.prevent="submit">

                            <validation-provider
                                v-slot="{ errors }"
                                name="Nombre"
                                rules="required|max:20"
                            >
                                <v-textarea
                                v-model="nombre"
                                :counter="20"
                                :error-messages="errors"
                                label="Nombre de la tecnologia"
                                required
                                ></v-textarea>
                            </validation-provider>

                            <validation-provider
                                v-slot="{ errors }"
                                name="Descripcion"
                                rules="required|max:400"
                            >
                                <v-textarea
                                v-model="descripcion"
                                :counter="400"
                                :error-messages="errors"
                                label="Descripción de la tecnologia"
                                required
                                ></v-textarea>
                            </validation-provider>                 
                            </form>

                            <v-btn
                              class="mr-4"                                
                              :disabled="invalid"
                              color="success"
                              @click="crear"
                            >
                              Agregar
                            </v-btn>
                            <v-dialog
                                v-model="dialog"
                                max-width="290"
                              >
                                <v-card>
                                  <v-card-title class="text-h5">
                                    Tecnologia agregada
                                  </v-card-title>

                                  <v-card-text>
                                    La tecnologia ha sido agregada con exito.
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
                        </validation-observer>

                    </v-card-text>
                </v-card>
                </v-stepper-content>
            </v-stepper>
        </v-container>
    </v-card>
</template>

<script>

import {mapGetters} from 'vuex'
import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'

setInteractionMode('eager')

extend('digits', {
...digits,
message: '{_field_} Necesita un largo de {length} digitos. ({_value_})',
})
extend('required', {
...required,
message: '{_field_} debe ser llenado',
})
extend('max', {
...max,
message: '{_field_} may not be greater than {length} characters',
})
extend('regex', {
...regex,
message: '{_field_} {_value_} does not match {regex}',
})
extend('email', {
...email,
message: 'El correo ingresado debe ser valido',
})

export default {  
    name: 'App',
    components: {
        ValidationProvider,
        ValidationObserver,
    },
    computed: {
        ...mapGetters(['user'])
    },
    data () {
        return {
            e6: 1,
            flag: 0,
            nombre: '',
            descripcion: '',
            dialog: false,
        }
    },
    methods:{
        crear: async function(){
          try{
            var result;
            result = await this.$http.post('/tecnologias/create',{
              nombre: this.nombre,
              descripcion: this.descripcion,
            });
            this.dialog = true;
            this.respuesta = result.data;
          }
          catch (error) {
            console.log('error', error);
          }
        },
        cerrar(){
          this.dialog = false;
          this.$router.push({name:'Home'});    
        },
    },
}

</script>