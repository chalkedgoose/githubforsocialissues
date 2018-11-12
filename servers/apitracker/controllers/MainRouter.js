const express = require('express');
const MainRouter = express.Router();
const mongoose = require('mongoose')
const Req = require('../models/req')


MainRouter.get('/requests', (req, res) => {
    /**
     * Gets all the requests back from the mongoDatabase and sends them to the client 
     */

    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");

    Req.find().lean().then(reqs => {
        res.json(reqs)
    }).catch(err => {
        res.send(err)
    });

})


module.exports = MainRouter