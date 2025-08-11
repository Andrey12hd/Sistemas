const express = require("express")
const app = express()
const port = 3000
app.use(express.json())
const usuarios = []
app.post('/usuarios', (req, res)=>{
    const usuario = req.body
    usuarios.push(usuario)
    res.send("Usuário cadastrado com sucesso")
})

app.get ('/usuarios', (req, res)=>{
    res.send(usuarios)
})
app.listen(port, ()=>{
    console.log("API rodando...")
})