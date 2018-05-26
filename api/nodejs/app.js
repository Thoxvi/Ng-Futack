let express = require('express');
let app = express();
let fs = require("fs");

app.get('/api/test', function (req, res) {
    res.end("hello world")
});

let server = app.listen(5000, function () {
});