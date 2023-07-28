const { Router } = require('express');
const SegurancaController = require('../controllers/seguranca/controller');


const router = Router();

router
    .post('/seguranca/acl', SegurancaController.createACL)
    .post('/seguranca/permissoes-roles', SegurancaController.createPermissionsRoles);


module.exports = router;