const bodyParser = require('body-parser');

const usuarios = require('./usuarios');
const auth = require('./auth');
const role = require('./role');
const permission = require('./permission')

module.exports = app => {
    app.use(
        bodyParser.json(),
        auth,
        usuarios,
        role,
        permission
    )
};
