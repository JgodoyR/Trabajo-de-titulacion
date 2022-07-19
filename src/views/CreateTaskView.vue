<template>
    <v-card color="blue darken-3" max-width="900" class="mx-auto">
        <v-container class="mt-5">
            <v-stepper v-model="e6" vertical>
                <v-stepper-step
                :complete="e6 > 1"
                step="1"
                >
                Creación de ejercicios
                </v-stepper-step>

                <v-stepper-content step="1">
                <v-card           
                    class="mb-12n"
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
                                name="Tecnologia"
                                rules="required"
                            >
                                <v-select
                                v-model="tecnologia_id"
                                :items="tecnologias"                                      
                                :error-messages="errors"
                                label="Tecnologia"
                                item-text="nombre"
                                item-value="id"
                                required
                                ></v-select>
                            </validation-provider>

                            <validation-provider
                                v-slot="{ errors }"
                                name="Nombre"
                                rules="required|max:100"
                            >
                                <v-textarea
                                id="nombre"
                                v-model="nombre"
                                :counter="100"
                                :error-messages="errors"
                                label="Nombre del ejercicio"
                                required
                                
                                ></v-textarea>
                            </validation-provider>

                            
                            <br>
                            <validation-provider
                                v-slot="{ errors }"
                                name="Enunciado"
                                rules="required|max:5000"
                            >
                              <h3 class="d-flex align-start">Enunciado</h3>
                              <quill-editor
                                label="Enunciado"
                                v-model="enunciado"
                                :content="content"
                                :options="editorOption"
                                @change="onEditorChange($event)"
                                :error-messages="errors"
                                :counter="5000"
                                required
                              />
                            </validation-provider>
                            <br>


                            <validation-provider
                                v-slot="{ errors }"
                                name="Respuesta"
                                rules="required|max:50"
                            >
                                <v-textarea
                                v-model="respuesta1"
                                :counter="50"
                                :error-messages="errors"
                                label="Respuesta al ejercicio"                                     
                                required 
                                ></v-textarea>
                            </validation-provider>

                            <validation-provider
                                v-slot="{ errors }"
                                name="Respuesta opcional"
                                rules="max:50"
                            >
                                <v-textarea
                                v-model="respuesta2"
                                :counter="50"
                                :error-messages="errors"
                                label="(Opcional) Respuesta extra al ejercicio"                                     
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
                              Crear
                            </v-btn>
                            <v-dialog
                                v-model="dialog"
                                max-width="290"
                              >
                                <v-card>
                                  <v-card-title class="text-h5">
                                    Ejercicio creado
                                  </v-card-title>

                                  <v-card-text>
                                    El ejercicio ha sido creado con exito.
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

import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

import { quillEditor } from 'vue-quill-editor'

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
message: 'El {_field_} del ejercicio no debe exceder los {length} caracteres',
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
        quillEditor
        
    },
    computed: {
        ...mapGetters(['user']),
        editor() {
          return this.$refs.myQuillEditor.quill
        }
    },
    data () {
        return {
            e6: 1,
            cant_ejercicios: null,
            tecnologia_id: null,
            flag: 0,
            nombre: '',
            enunciado: '',
            respuesta1: '',
            respuesta2: '',
            tecnologias: [],
            estudiantes: [],
            dialog: false,
            content: '',
            editorOption: {
              
            }
        }
    },
    methods:{
      getData: async function(){
          if (this.user==null)
            this.$router.push('/');
          if (this.user.rol!=1 && this.user.rol!=2)
            this.$router.push('/');
            try {
                var result = await this.$http.get('/tecnologias/all');
                let response = result.data;
                this.tecnologias = response;    
                
                var result2 = await this.$http.get('/contar_ejercicios');
                let response2 = result2.data;
                this.cant_ejercicios = response2;

                var result3 = await this.$http.get('/estudiantes');
                let response3 = result3.data;
                this.estudiantes = response3; 

            } catch (error) {
                console.log('error', error);
            }
        },
        crear: async function(){
          try{
            var result;
            result = await this.$http.post('/ejercicios/create',{
              tecnologia: this.tecnologia_id,
              nombre: this.nombre,
              enunciado: this.enunciado,
              respuesta1: this.respuesta1,
              respuesta2: this.respuesta2,
            });
            this.dialog = true;
            this.respuesta = result.data;
          
            for(var k = 0; k < this.estudiantes.length; k++){
              if(this.estudiantes[k].rol == 3){
                var result2;
                result2 = await this.$http.post('/usuario_ejercicio/create',{
                  usuario: this.estudiantes[k].id,
                  ejercicio: this.cant_ejercicios + 1,
                  tiempo: null,
                  estado: 0,
                  respuesta: null
                });
                this.respuesta2 = result2.data;
              }
            }
          }
          catch (error) {
            console.log('error', error);
          }
        },
        cerrar(){
          this.dialog = false;
          this.$router.push({name:'Home',params:{id:this.tecnologia_id}});    
        },
        onEditorBlur(quill) {
          console.log('editor blur!', quill)
        },
        onEditorFocus(quill) {
          console.log('editor focus!', quill)
        },
        onEditorReady(quill) {
          console.log('editor ready!', quill)
        },
        onEditorChange({ quill, html, text }) {
          console.log('editor change!', quill, html, text)
          this.content = html
        }
    },
    created:function(){
        this.getData();
    },
    mounted() {
      console.log('this is current quill instance object', this.editor)
    }

}

</script>