const { Router } = require('express');
const Controller = require('../controllers/permission/controller')

const router = Router();

router
    .post('/permissao', Controller.createPermission)
    .get('/permissao', Controller.getAllPermissions)
    .get('/permissao/:id')
    .delete('/permissao/:id')
    .put('/permissao/:id')

module.exports = router