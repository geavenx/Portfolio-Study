const database = require('../models');
const Sequelize = require('sequelize');

class SegurancaService {
    async createACL(data) {
        try {
            const usuario = await database.usuarios.findOne({
                include: [
                    {
                        model: database.roles,
                        as: 'usuario_roles',
                        attributes: ['id', 'nome', 'descricao'],
                    },
                    {
                        model: database.permissoes,
                        as: 'usuario_permissoes',
                        attributes: ['id', 'nome', 'descricao'],
                    },
                ],
                where: {
                    id: data.userId
                }
            })
            if(!usuario) {
                console.log(data.userId)
                throw new Error('Usuário não encontrado');
            }
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

            await usuario.removeUsuario_roles(usuario.usuario_roles);
            await usuario.removeUsuario_permissoes(usuario.usuario_permissoes);

            await usuario.addUsuario_roles(createdRoles);
            await usuario.addUsuario_permissoes(createdPermissoes);
            const newUser = await database.usuarios.findOne({
                include: [
                    {
                        model: database.roles,
                        as: 'usuario_roles',
                        attributes: ['id', 'nome', 'descricao'],
                    },
                    {
                        model: database.permissoes,
                        as: 'usuario_permissoes',
                        attributes: ['id', 'nome', 'descricao'],
                    }
                ]
                }
            )
            return newUser;
        } catch(err) {
            console.log(`Mensagem de erro: ${err}`)
            console.log(`role: ${data.role}\npermissao: ${data.permissao}`)
            throw new Error(err);
        }            
    }
    
    async createPermissionsRoles(data) {
        const role = await database.roles.findOne({
            include: [
                {
                    model: database.permissoes,
                    as: 'role_da_permissao',
                    attributes: ['id', 'nome', 'descricao'],
                    through: {
                        attributes: [],
                    }
                }
            ]});
        if (!role) {
            throw new Error('Role not found');
        }

        const createdPermissions = await database.permissoes.findAll({
            where: {
                id: {
                    [Sequelize.Op.in]: data.permissoes
                }
            }
        });
        
        await role.removeRole_da_permissao(role.role_da_permissao);
        await role.addRole_da_permissao(createdPermissions);

        const newRole = await database.roles.findOne({
            include: [
                {
                    model: database.permissoes,
                    as: 'role_da_permissao',
                    attributes: ['id', 'nome', 'descricao'],
                    through: {
                        attributes: [],
                    }
                }],
                where: {
                    id: data.roleId
                }
        });
        return newRole;
    }
}
module.exports = SegurancaService;
