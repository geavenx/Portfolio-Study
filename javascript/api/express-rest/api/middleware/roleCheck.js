const database = require("../models");

const roles = (listaRoles) => {
	return async (req, res, next) => {
		/* ----- recebe o userId da requisição ----- */
		const { userId } = req;

		/* ----- busca as roles do usuário -----*/
		const user = await database.usuarios.findOne({
			include: [
				{
					model: database.roles,
					as: "usuario_roles",
					attributes: ["id", "nome"]
				}
				],
			where: {
				id: userId
			}
		});

		/* ----- valida se o usuário existe -----*/
		if (!user) {
			return res.status(400).send({ message: "User not found" })
		};

		/* ----- criando um array com todas as roles cadastradas no usuário -----*/
		const userRoles = user.usuario_roles
			.map((role) => role.nome) // <-- retorna um array das roles do usuário;
			.some((role) => listaRoles.includes(role)); // <-- verifica se o usuário tem a role passada para o middleware;

		if (!userRoles) {
			return res.status(401).send({ message: "User not authorized" })
		};

		return next();
	}
}

module.exports = roles;