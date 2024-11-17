const express = require("express");
const path = require("path");
const { spawn } = require('child_process');
const app = express();

app.set("view engine", "ejs")

app.use(express.urlencoded({ extended: true }));

app.get('/', function (req, res) {
    res.render("index",{result: null , segment: 0});
})

app.post('/register', function (req, res) {
    var t = req.body.analyse;
    var m = req.body.marks;
    console.log(m);
    var text = "" + t;
    if (text.length == 0) res.send("Enter some text");
    const pythonProcess = spawn('python3', ['python.py', text, m]);

    let output = '';
    pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
    });

    pythonProcess.stderr.on('data', (error) => {
        console.error(`Error from Python script: ${error}`);
    });

    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: 'Internal server error in Python script' });
        }
        try {
            res.render("index",{result : output, segment: 0})
        } catch (err) {
            res.status(500).json({ error: 'Error parsing Python output' });
        }
    });
})

app.listen(4500)