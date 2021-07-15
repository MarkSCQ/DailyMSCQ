const express = require('express')

const app = express()

app.get('/', (request, response) => {
    response.send("HELLO EXPRESS")
})

app.listen(8000, () => {
    console.log("Express is running , 8000 is used")
})

