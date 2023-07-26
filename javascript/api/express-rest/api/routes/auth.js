const { Router } = require('express');
const AuthController = require('../controllers/auth/controllers')

const router = Router();

router
    .post('/auth/login', AuthController.login)

module.exports = router;