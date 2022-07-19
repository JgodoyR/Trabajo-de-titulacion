<template>
    <form @submit.prevent="handleSubmit">
        <errorAlert v-if="errorAlert" :errorAlert="errorAlert"/>
        <v-main>
            <v-card width="500" class="mx-auto mt-9">
                <v-card-title class="justify-center"> Ingrese a su cuenta </v-card-title>
                <v-card-text>
                    <v-text-field label="Rut" class="form-control" v-model="rut" prepend-icon="mdi-account-circle"/>
                    <v-text-field label="Password" class="form-control" v-model="password"  
                    :type="showPassword ? 'text' : 'password'" prepend-icon="mdi-lock" 
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" 
                    @click:append="showPassword = !showPassword"
                    @keyup.enter="handleSubmit"/>
                </v-card-text>

                <v-divider></v-divider>
                <v-card-actions class="justify-center">
                    <v-btn color="blue" @click="handleSubmit" > Ingresar </v-btn>
                </v-card-actions>
            </v-card>
        </v-main>
    </form>
</template>

<script>
import ErrorAlert from './ErrorAlert.vue'

    export default {

        name: 'LoginView',
        components: {ErrorAlert},
        data: function () {
            return {
                errorAlert: '',
                rut: '',
                password: '',
                showPassword: false
            }
        },
        methods: {
            handleSubmit: async function(){
                try{
                    var result = await this.$http.post('/login',{
                        rut: this.rut,
                        password: this.password
                    });
                    let response = result.data;
                    localStorage.setItem('token', response.jwt);
                    this.$cookies.set("token", response);

                    var result2 = await this.$http.post('/user', response);
                    let response2 = result2.data;
                    this.$store.dispatch('user', response2);
                    this.$router.push('/');
                }
                catch (e){
                    this.errorAlert = 'Usuario/Contraseña erroneas'
                }
            }
        },

    }

</script>