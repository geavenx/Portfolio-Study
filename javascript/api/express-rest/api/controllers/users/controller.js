const GetService = require('../../services/DbServices');
const getService = new GetService();

class Controllers {
    static async getAllUsers(req, res) {
        const users = await getService.getAllUsers()
        res.status(200).json(users) // SUCCESS
    }

    static async createUser(req, res) {
        const { nome, email, senha } = req.body;
       
        try {
            const user = await getService.createUser({ nome, email, senha })

            res.status(201).json(user); // SUCCESS
        } catch(err) {
            console.log(`Erro ao cadastrar usuário ${err.message}`)
            res.status(400).send({ // ERROR
                message: err.message
            })
       }
    }

    static async getByID(req, res) {
        const { id } = req.params;
        try {
            const user = await getService.getUserByID(id)
            res.status(200).json(user); // SUCCESS
        } catch(err) {
            console.log(`Erro ao identificar usuário ${err.message}`)
            res.status(400).send({ // ERROR
                message: err.message
            })
        }
    }
    
    static async updateUser(req, res) {
        const { nome, email, senha } = req.body;
        const { id } = req.params;
        try {
            const user = await getService.updateUser(id, { nome, email, senha })
            res.status(200).send({ // SUCCESS
                message: "User successfully updated"
            });
        } catch(err) {
            console.log(`Erro ao atualizar usuário: ${err.message}`);
            res.status(400).send({ // ERROR
                message: err.message
            })
        }
    }

    static async deleteUser(req, res) {
        const { id } = req.params;
        try {
            const user = await getService.deleteUser(id)
            res.status(200).send({ // SUCCESS
                message: "User successfully deleted"
            });
        } catch (err) {
            console.log(`Erro ao deletar usuário ${err.message}`);
            res.status(400).send({ // ERROR
                message: err.message
            })
        }
    }
}

module.exports = Controllers;
