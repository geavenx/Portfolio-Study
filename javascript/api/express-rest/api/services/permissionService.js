const { deletePermission } = require('../controllers/permission/controller');
const database = require('../models');
const { v4: uuidv4 } = require('uuid')

class PermissionService {
    async createPermission(data) {
        try {
            const permission = await database.permissoes.create({
                id: uuidv4(),
                nome: data.nome,
                descricao: data.descricao
            })
            return permission
        } catch (err) {
            throw new Error(`Error trying to create permission ${err.message}`)
        }
    }

    async getAllPermissions() {
        const permissions = await database.permissoes.findAll();
        return permissions;
    }
    
    async getPermissionById(id) {
        try {
            const permission = await database.permissoes.findOne({
                where: {
                    id: id
                }
            });
            if (!permission) {
                throw new Error('Permission not found');
            }
            return permission;
            
        } catch (err) {
            throw new Error(`Error trying to get permission ${err.message}`)
        }
    }
    
    async deletePermission(id) {
        try {
            const permission = await database.permissoes.destroy({
                where: {
                    id: id
                }
            });
            if (!permission) {
                throw new Error('Permission not found');
            }
            return permission;
            
        } catch (err) {
            throw new Error(`Error trying to delete permission ${err.message}`)
        }
    }
    
    async updatePermission(id, data) {
        try {
            const permission = await database.permissoes.update({
                nome: data.nome,
                descricao: data.descricao
            }, {
                where: {
                    id: id
                }
            });
            if (!permission) {
                throw new Error('Permission not found');
            }
            return permission;
            
        } catch (err) {
            throw new Error(`Error trying to update permission ${err.message}`)
        }
    }
}

module.exports = PermissionService
