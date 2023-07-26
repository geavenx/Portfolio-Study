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
}

module.exports = PermissionService