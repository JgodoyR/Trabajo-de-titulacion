<template>
    <div id="terminal-container-p"></div>
</template>

<script>

import '../../node_modules/xterm/lib/xterm.js'
import { Terminal } from 'xterm'
import { AttachAddon } from 'xterm-addon-attach'
import { FitAddon } from 'xterm-addon-fit'

  export default {
    name: 'TerminalCompP',
    data: () => ({
      drawer: false,
    }),
    mounted(){
        var term = new Terminal({
            cursorBlink: true,
            applicationCursor: true,
            fontSize: 20,
            rows: 30,
            cols: 130,
        });

        var socket = new WebSocket(`ws://localhost:2375/containers/docker/attach/ws?logs=0&stream=1&stdin=1&stdout=1&stderr=1`);
        var attachAddon = new AttachAddon(socket);
        var fitAddon = new FitAddon();

        term.loadAddon(attachAddon);
        term.loadAddon(fitAddon);

        term.open(document.getElementById('terminal-container-p'));

        fitAddon.fit()
        term.focus()
        socket.onopen = () => {socket.send('\n')}

        window.onresize = function(){
            fitAddon.fit()
        }

        this.term = term
        this.socket = socket

    },
    
    beforeDestroy(){
        this.socket.close()
        this.term.dispose()
    }

  }
</script>

<style>
@import '../../node_modules/xterm/css/xterm.css';
    div.terminal-container{
        width: 100%;
        height: 150%;
    }
</style>