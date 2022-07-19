<template>
    <v-container justify="center" style="margin-top:10px;">
        <h1>Playgrounds</h1>
        <v-row justify="center" style="margin-top:20px;">
            <terminal-comp-playground></terminal-comp-playground>
        </v-row>
    </v-container>
</template>

<script>
import TerminalCompPlayground from '../components/TerminalCompPlayground.vue'
import {mapGetters} from 'vuex'

export default {

    name: 'App',
    components: {TerminalCompPlayground},
    computed: {
        ...mapGetters(['user'])
    }
}
</script>