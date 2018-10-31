const mongoose = require('mongoose');




// method = StringField(required=True)
// endpoint = StringField(required=True)
// ip = StringField()
// accessed_on = DateTimeField(default=datetime.now)



const reqSchema = mongoose.Schema({
    method: {
        type: String,
        required: true
    },
    endpoint: {
        type: String,
        required: true
    },
    ip: {
        type: String
    },
    accessed_on: {
        type: Date,
        default: Date.now
    }
});

const req = mongoose.model('req', reqSchema);


module.exports = req;