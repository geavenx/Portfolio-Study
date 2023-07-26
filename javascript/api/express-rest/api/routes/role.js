const { Router } = require('express');
const Controllers = require('../controllers/role/controller');
const authenticated = require('../middleware/authenticated');

const router = Router();

router.use(authenticated)

router
    .post('/role', Controllers.createRole)
    .get('/role', Controllers.showRoles)
    .get('/role/:id', Controllers.showRoleByID)
    .delete('/role/:id', Controllers.deleteRole)
    .put('/role/:id', Controllers.updateRole)

module.exports = router;