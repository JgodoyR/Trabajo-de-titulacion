<template>
    <div id="terminal-container"></div>
</template>

<script>

import '../../node_modules/xterm/lib/xterm.js'
import { Terminal } from 'xterm'
import { AttachAddon } from 'xterm-addon-attach'
import { FitAddon } from 'xterm-addon-fit'

  export default {
    name: 'TerminalComp',
    data: () => ({
      drawer: false,
    }),
    mounted(){
        var term = new Terminal({
            cursorBlink: true,
            applicationCursor: true,
            fontSize: 20,
            rows: 30,
            cols: 90,
        });

        var socket = new WebSocket(`ws://localhost:2375/containers/docker/attach/ws?logs=0&stream=1&stdin=1&stdout=1&stderr=1`);
        var attachAddon = new AttachAddon(socket);
        var fitAddon = new FitAddon();

        term.loadAddon(attachAddon);
        term.loadAddon(fitAddon);

        term.open(document.getElementById('terminal-container'));

        fitAddon.fit()
        term.focus()
        socket.onopen = () => {socket.send('\n')}

        window.onresize = function(){
            fitAddon.fit()
        }

        this.term = term
        this.socket = socket

        //term.open(document.getElementById('terminal-container'));
        /*var buff = '';

        term.prompt = () => {
            term.write("\r~$ ");
        };
        `Terminal  \n`
        .split("\n")
        .map(line => term.writeln(line));
        term.prompt();
        term.onKey( ev => {
            console.log(ev.key)
            const printable = !ev.domEvent.altKey && !ev.domEvent.altGraphKey && !ev.domEvent.ctrlKey && !ev.domEvent.metaKey;
            if (ev.key == '\r') {
                if(buff == "clear"){
                    buff = '';
                    term.clear();
                }
                term.writeln('');
                term.prompt();
                buff = '';
            } else if (ev.key == '\b') {
                buff = buff.slice(0, -1);
                if (term.buffer.x > 3) {
                    term.write("\b \b");
                }
            } else if (printable) {
                buff += ev.key;
                //term.write(ev.key);
            } else if(ev.key.charCodeAt === 38 || ev.key.charCodeAt === 40 || ev.key.charCodeAt < 32){
                return;
            }
        });

        term.onData(function(data) {
            console.log(data);
            term.write(data);
        });*/
    },
    
    beforeDestroy(){
        this.socket.close()
        this.term.dispose()
    }

    /*
        var socket = new WebSocket('ws://localhost:2375/containers/jenkins2/attach/ws?logs=0&stream=1&stdin=1&stdout=1&stderr=1');
        var attachAddon = new AttachAddon(socket);
        var fitAddon = new FitAddon();

        term.loadAddon(attachAddon);
        term.loadAddon(fitAddon);

        term.open(document.getElementById('terminal-container'));

        fitAddon.fit()
        term.focus()
        socket.onopen = () => {socket.send('\n')}

        window.onresize = function(){
            fitAddon.fit()
        }

        this.term = term
        this.socket = socket*/
        
/*
        term.open(document.getElementById('terminal-container'));
        var buff = '';

        term.prompt = () => {
        term.write("\r~$ ");
        };
        `Terminal  \n`
        .split("\n")
        .map(line => term.writeln(line));
        term.prompt();
        term.on("key", (key, ev) => {
            const printable = !ev.altKey && !ev.altGraphKey && !ev.ctrlKey && !ev.metaKey;
            if (ev.keyCode === 13) {
                if(buff == "-help"){
                    term.write("\r\ncomando escrito correctamente\r\n");
                }
                else{
                    term.write("\r\ncomando desconocido\r\nescriba -help\r\n");
                }
                term.writeln('');
                term.prompt();
                buff = '';
            } else if (ev.keyCode === 8) {
                buff = buff.slice(0, -1);
                if (term.buffer.cursorX > 3) {
                    term.write("\b \b");
                }
            } else if (printable) {
                buff += key;
                term.write(key);
            } else if(ev.keyCode === 38 || ev.keyCode === 40 || ev.keyCode === 127){
                return;
            }
        });

        term.on("paste", function(data) {
            term.write(data);
        });*/
  }
</script>

<style>
@import '../../node_modules/xterm/css/xterm.css';
    div.terminal-container{
        width: 100%;
        height: 150%;
    }
</style>