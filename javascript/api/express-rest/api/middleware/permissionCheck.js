const database = require('../models');

const permissoes = (listaPermissoes) => {
	return async (req, res, next) => {
		/* ----- recebe userId da requisição ----- */
		const { userId } = req;

		/* ----- busca o usuário e todas as suas permissões ----- */
		const user = await database.usuarios.findOne({
			include: [
			{
				model: database.permissoes,
				as: "usuario_permissoes",
				attributes: ["id", "nome"]
			}],
			where: {
				id: userId
			}
		});

		/* ----- valida se o usuário existe ----- */
		if (!user) {
			return res.status(400).send({ message: "User not found" })
		};

		/* ----- valida se as permissões do usuário são as mesmas que as permitidas na rota ----- */
		const createdPermissions = user.usuario_permissoes
			.map((permission) => permission.nome)
			.some((permission) => listaPermissoes.includes(permission));

		/* ----- se usuário não for permitido na rota, retornar 401 ----- */
		if (!createdPermissions) {
			return res.status(401).send({ message: "User not authorized" })
		};

		/* ----- caso contrário, prosseguir normalmente ----- */
		return next();
	}
}

module.exports = permissoes;