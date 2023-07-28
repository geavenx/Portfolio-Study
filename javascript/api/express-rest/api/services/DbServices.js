const { v4: uuidv4 } = require('uuid');
const database = require('../models');
const { hash } = require('bcrypt');

class Services{
    async getAllUsers() {
        const users = await database.usuarios.findAll({
            include: [
                {
                    model: database.roles,
                    as: 'usuario_roles',
                    attributes: ['id', 'nome', 'descricao'],
                    through: {
                        attributes: [],
                    }
                },
                {
                    model: database.permissoes,
                    as: 'usuario_permissoes',
                    attributes: ['id', 'nome', 'descricao'],
                    through: {
                        attributes: [],
                    }
                }
            ]
        });

        return users;
    }
    async createUser(data) {
        const user = await database.usuarios.findOne({
            where: {
                nome: data.nome
            }
        })
        if (user) {
            throw new Error('User already exists');
        }
        
        const senhaHash = await hash(data.senha, 8)

        try {
            const newUser = await database.usuarios.create({
              id: uuidv4(),
              nome: data.nome,
              email: data.email,
              senha: senhaHash 
            });

            return newUser;
        } catch(err) {
            console.error(`Erro ao cadastrar usuário: ${err.message}`);
            throw err;
        }
    }
    
    async getUserByID(id) {
        const user = await database.usuarios.findOne({
            where: {
                id: id
            }
        })
        if (!user) {
            throw new Error('Cannot find user');
        } else {
            return user;
        } 
    }
    async updateUser(id, data) {
        const userExists = await database.usuarios.findOne({
            where: {
                id: id
            }
        })
        if (!userExists) {
            throw new Error('Cannot find user');
        }
        
        const senhaHash = hash(data.senha, 8);
        
        try {
            const user = await database.usuarios.update({
                nome: data.nome,
                email: data.email,
                senha: senhaHash
            }, {
                where: {
                    id: id
                }});
            return user;

        } catch(err) {
            console.error(`Erro ao atualizar usuario: ${err.message}`);
            throw err;
        }
    }
    
    async deleteUser(id) {
        const userExists = await database.usuarios.findOne({
            where: {
                id: id
            }
        })
        if (!userExists) {
            throw new Error('Cannot find user');
        }
        try {
            const user = await database.usuarios.destroy({
                where: {
                    id: id
                }
            })
            return user;
        } catch (err) {
            console.error(`Erro ao deletar usuário: ${err.message}`);
            throw err;
        }
        
    }
}

module.exports = Services;
