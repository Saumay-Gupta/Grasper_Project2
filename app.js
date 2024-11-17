const express = require("express");
const path = require("path");
const { spawn } = require('child_process');

const app = express();
app.set("view engine", "ejs")
app.use(express.static('public'))
app.use(express.urlencoded({ extended: true }));

app.get('/', function (req, res) {
    res.render("index", { segment: '', key: '', entity: '', total: "" ,flash:"",select:''});
})

app.post('/analyse', function (req, res) {
    var t = req.body.input;
    var text = "" + t;
    if (text.length == 0) res.render("index", { segment: '', key: '', entity: '', total: "" , flash:'Enter some text please',select:''});
    var m = req.body.marks;
    if(typeof(m)=="undefined") res.render("index", { segment: '', key: '', entity: '', total: text , flash:'',select:'Select One of the above'});
    var s = m.toString();
    console.log(text.length)
    const pythonProcess = spawn('python3', ['python.py', text, s]);

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
            const parsedOutput = JSON.parse(output);
            var s = parsedOutput.segment || '';
            var k = parsedOutput.key || '';
            var e = parsedOutput.entity || '';
            k = JSON.stringify(k);
            const arr_e = [];
            for (var key in e) {
                arr_e.push([key, e[key]]);
            }
            res.render("index", { segment: s, key: k.slice(1, -1).trim(), entity: arr_e, total: text ,flash:'',select:''});
        } catch (err) {
            res.status(500).json({ error: 'Error parsing Python output' });
        }
    });
})

app.listen(5500)
