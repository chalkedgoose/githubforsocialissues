const express = require('express');
const MainRouter = express.Router();
const mongoose = require('mongoose')
const circularJSON = require('circular-json');
const Req = require('../models/req')


MainRouter.get('/requests', (req, res) => {
    /**
     * Gets all the requests back from the mongoDatabase and sends them to the client 
     */
    Req.find().lean().then(reqs => {
        res.json(reqs)
    }).catch(err => {
        res.send(err)
    });

})


module.exports = MainRouter