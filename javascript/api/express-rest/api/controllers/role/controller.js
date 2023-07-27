const RoleService = require('../../services/roleService');
const roleService = new RoleService();

class RoleController {
    static async createRole(req, res) {
        const { nome, descricao } = req.body;

        try {
            const role = await roleService.create({ nome, descricao });
            res.status(201).send(role)
        } catch (err) {
            res.status(400).send({
                message: err.message
            })
        }
    }
    
    static async showRoles(req, res) {
        try {
            const roles = await roleService.getAllRoles();
            res.status(200).json(roles); 
        } catch (err) {
            console.log(`Erro ao mostrar roles: ${err.message}`)
            res.status(400).send({
                message: err.message
            })
        }
    } 
    
    static async showRoleByID(req, res) {
        const { id } = req.params;
        try {
            const role = await roleService.getRoleByID(id);
            res.status(200).json(role);
       } catch (err) {
            console.log(`Erro ao encontrar role por ID: ${err.message}`)
            res.status(400).send({
                message: err.message
            }) 
       } 
    }

    static async deleteRole(req, res) {
       const { id } = req.params;
       try {
            const role = await roleService.deleteRole(id);
            res.status(200).send({
                status: role,
                message: "Role successfully deleted."
            })
       } catch (err) {
            console.log(`Erro ao delear role: ${err.message}`)
            res.status(400).send({
                message: err.message
            })
       } 
    }
    
    static async updateRole(req, res) {
       const { nome, descricao } = req.body;
       const { id } = req.params;
       
       try {
            const updatedRole = await roleService.updateRole(id, { nome, descricao });
            res.status(200).send({
                message: "Role successfully updated.",
                status: updatedRole,
                new_data: {
                    nome: nome,
                    descricao: descricao
                }
                
            });
        } catch (err) {
            console.log(`Erro ao atualizar role: ${err.message}`);
            res.status(400).send({
                message: err.message
            })
        }
    }
}

module.exports = RoleController