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
}

module.exports = PermissionController