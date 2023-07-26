const database = require('../models');
const { compare } = require('bcrypt');
const { sign } = require('jsonwebtoken');
const jsonSecret = require('../config/jsonSecret');

class AuthService {
    async login(data) {
       const user = await database.usuarios.findOne({
        attributes: ['id', 'email', 'senha'],
        where: {
            email: data.email
        }
       });
       if(!user) {
        throw new Error('Cannot find user')
       }
       
       const equalPasswords = await compare(data.senha, user.senha);
       if (!equalPasswords) {
        throw new Error('Incorrect credentials');
       }
        
       const accessToken = sign({
        id: user.id,
        email: user.email
       }, jsonSecret.secret, {
        expiresIn: 86400
       })

       return { accessToken }
    }
}

module.exports = AuthService;
