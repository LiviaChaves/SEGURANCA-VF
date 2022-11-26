//https://nodejs.org/en/knowledge/HTTP/servers/how-to-create-a-HTTPS-server/
//https://nodejs.org/api/https.html
//https://www.digitalocean.com/community/tutorials/use-expressjs-to-deliver-html-files
//para executar digitar : node questao02.js no terminal 
// Certificado foi gerado utilizando o OPENSSL 


const fs = require('fs')
const path = require('path')
const https = require('https')
const express = require('express')
const porta = 8000
const app = express()


app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, '/index.html'))
})

https.createServer({
    key: fs.readFileSync('key.pem'), 
    cert: fs.readFileSync('cert.pem') 
}, app).listen(porta)
console.log('link Servidor https://localhost:' + porta)