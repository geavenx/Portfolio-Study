'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class usuarios extends Model {
    static associate(models) {
      usuarios.belongsToMany(models.permissoes, {
        through: models.usuario_permissao,
        as: 'usuario_permissoes',
        foreignKey: 'usuario_id'
      });
      usuarios.belongsToMany(models.roles, {
        through: models.usuario_role,
        as: 'usuario_roles',
        foreignKey: 'usuario_id'
      });
    }
  }
  usuarios.init({
    nome: DataTypes.STRING,
    email: DataTypes.STRING,
    senha: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'usuarios',
    defaultScope: {
      attributes: { exclude: ['senha'] }
    }
  });
  return usuarios;
};