const express = require('express');
const app = express();
const mongoose = require('mongoose');
const config = require('./config.js');
const MainRouter = require('./controllers/MainRouter.js');

/**
 * Connecting to the MongoDatabase
 */


mongoose.connect(config.MongoURI, { useNewUrlParser: true })
    .catch(
        (err) => {
            throw err;
        }
    )


/**
 * API Main Router.
 */
app.use('/', MainRouter);

/**
 * Starting Service.
 */
app.listen(config.PORT, () => {
    console.log(` This application is running on ${config.PORT}`);
})






