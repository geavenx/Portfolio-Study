const { Router } = require('express');
const Controller = require('../controllers/permission/controller')

const router = Router();

router
    .post('/permissao', Controller.createPermission)
    .get('/permissao', Controller.getAllPermissions)
    .get('/permissao/:id', Controller.getPermissionById)
    .delete('/permissao/:id', Controller.deletePermission)
    .put('/permissao/:id', Controller.updatePermission)

module.exports = router