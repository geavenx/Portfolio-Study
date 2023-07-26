const { Router } = require('express');
const Controllers = require('../controllers/users/controller');
const authenticated = require('../middleware/authenticated');

const router = Router()

router.use(authenticated);

router
    .get('/usuarios', Controllers.getAllUsers)
    .get('/usuarios/id/:id', Controllers.getByID)
    .post('/usuarios', Controllers.createUser)
    .put('/usuarios/id/:id', Controllers.updateUser)
    .delete('/usuarios/id/:id', Controllers.deleteUser)

module.exports = router;