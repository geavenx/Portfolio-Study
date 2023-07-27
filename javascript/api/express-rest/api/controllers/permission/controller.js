const PermissionService = require('../../services/permissionService');

const permissionService = new PermissionService()

class PermissionController {
    static async createPermission(req, res) {
        const { nome, descricao } = req.body;
        
        try {
            const permission = await permissionService.createPermission({ nome, descricao })
            res.status(201).json(permission);
        } catch (err) {
            console.log(`Error trying to create permission ${err.message}`);
            res.status(400).send({
                message: err.message
            })
        }
    }
    
    static async getAllPermissions(req, res) {
       const permissions = await permissionService.getAllPermissions();
       res.status(200).json(permissions); 
    }
    
    static async getPermissionById(req, res) {
        try {
            const { id } = req.params;
            const permission = await permissionService.getPermissionById(id);
            res.status(200).json(permission);
        } catch (err) {
            console.log(`Error trying to get permission ${err.message}`);
            res.status(400).send({
                message: err.message
            })
        }
    }
    
    static async deletePermission(req, res) {
        try {
            const { id } = req.params;
            const permission = await permissionService.deletePermission(id);
            res.status(200).json(permission);
        } catch (err) {
            console.log(`Error trying to delete permission ${err.message}`);
            res.status(400).send({
                message: err.message
            })
        }
    }
    
    static async updatePermission(req, res) {
        try {
            const { id } = req.params;
            const { nome, descricao } = req.body;
            const permission = await permissionService.updatePermission(id, { nome, descricao });
            res.status(200).json(permission);
        } catch (err) {
            console.log(`Error trying to update permission ${err.message}`);
            res.status(400).send({
                message: err.message
            })
        }
    }
}

module.exports = PermissionController