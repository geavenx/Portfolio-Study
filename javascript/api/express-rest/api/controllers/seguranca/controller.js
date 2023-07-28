const SegurancaService = require('../../services/segurancaService');
const segurancaService = new SegurancaService;

class SegurancaController {
    static async createACL(req, res) {
        const { role, permissao } = req.body;
        const { userId } = req;

        try {
            const acl = await segurancaService.createACL({ role, permissao, userId });
            
            res.status(201).send(acl);
        } catch (err) {
            res.status(400).send({ message: err.message });
        }
    }
    
    static async createPermissionsRoles(req, res) {
        const { roleId, permissoes } = req.body;
        try{
            const createdPermissions = await segurancaService.createPermissionsRoles({ roleId, permissoes });
            res.status(200).send(createdPermissions);
        } catch (err) {
            res.status(400).send({ message: err.message });
        }
    }    
}

module.exports = SegurancaController;