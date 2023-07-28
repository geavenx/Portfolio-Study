const { Router } = require('express');
const Controller = require('../controllers/permission/controller')
const permission = require('../middleware/permissionCheck')

const router = Router();

router
    .post('/permissao', permission(["test"]), Controller.createPermission)
    .get('/permissao', Controller.getAllPermissions)
    .get('/permissao/:id', Controller.getPermissionById)
    .delete('/permissao/:id', Controller.deletePermission)
    .put('/permissao/:id', Controller.updatePermission)

module.exports = router