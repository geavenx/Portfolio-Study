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
}

module.exports = SegurancaController;