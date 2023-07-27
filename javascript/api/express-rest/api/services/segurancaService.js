const database = require('../models');
const Sequelize = require('sequelize');

class SegurancaService {
    async createACL(data) {
        try{
            const usuario = await database.usuarios.findOne({
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
                ],
                where: {
                    id: data.userId
                }
            })
        } catch (err) {
            console.log(`Error trying to find user: ${err.message}`);
            throw new Error(err.message);
        }
        if(!usuario) {
            console.log(data.userId)
            throw new Error('Usuário não encontrado');
        }
        try {
            const createdRoles = await database.roles.findAll({
                where: {
                    id: {
                        [Sequelize.Op.in]: data.role
                    }
                }
            })
            const createdPermissoes = await database.permissoes.findAll({
                where: {
                    id: {
                        [Sequelize.Op.in]: data.permissao
                    }
                }
            });
        } catch (err) {
            console.log(`Error trying to find perms/roles: ${err.message}`);
            throw new Error(err.message);
        }

        try {
            await usuario.removeUsuario_roles(usuario.usuario_roles);
            await usuario.removeUsuario_permissoes(usuario.usuario_permissoes);

            await usuario.addUsuario_roles(createdRoles);
            await usuario.addUsuario_permissoes(createdPermissoes);
        } catch (err) {
            console.log(`aaa: ${err.message}`);
            throw new Error(err.message);
        }
        try { 
            const newUser = await database.usuarios.findOne({
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
                }
            )
        } catch (err) {
            console.log(`Error trying to find user: ${err.message}`);
            throw new Error(err.message);
        }
            
        return newUser;
    }
}
module.exports = SegurancaService;
