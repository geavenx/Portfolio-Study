const database = require('../models');
const { v4: uuidv4 } = require('uuid');

class RoleService {
    async create(data) {
        const role = await database.roles.findOne({
            where: {
                nome: data.nome
            }
        }) 
        
        if (role) {
            throw new Error("Role already exists");
        }

        try {
            const newRole = await database.roles.create({
                id: uuidv4(),
                nome: data.nome,
                descricao: data.descricao
            });
            return newRole;

        } catch (err) {
            throw new Error("Error creating role")
        }
    }

    async getAllRoles() {
        const roles = await database.roles.findAll();
        return roles;
    }
    
    async getRoleByID(id) {
        const role = await database.roles.findOne({
            where: {
                id: id
            }
        })
        if (!role) {
            throw new Error('Cannot find role');
        } else {
            return role;
        } 
    }
    
    async deleteRole(id) {
        const roleExists = await database.roles.findOne({
            where: {
                id: id
            }
        })
        if (!roleExists) {
            throw new Error('Cannot find role');
        }
        try {
            const role = await database.roles.destroy({
                where: {
                    id: id
                }
            })
            return role;
        } catch (err) {
            console.error(`Erro ao deletar role: ${err.message}`);
            throw err;
        }
    }
    
    async updateRole(id, data) {
        const roleExists = await database.roles.findOne({
            where: {
                id: id
            }
        })
        if (!roleExists) {
            throw new Error('Cannot find role');
        }
        
        try {
            const role = await database.roles.update({
                nome: data.nome,
                descricao: data.descricao
            }, {
                where: {
                    id: id
                }});
            return role;

        } catch(err) {
            console.error(`Erro ao atualizar role: ${err.message}`);
            throw err;
        }
    }
}

module.exports = RoleService