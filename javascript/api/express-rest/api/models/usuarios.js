'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class usuarios extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      usuarios.belongsToMany(models.roles, {
        through: 'usuarios_roles',
        as: 'usuarios_roles',
        foreignKey: 'usuario_id'
      })
      usuarios.belongsToMany(models.permissoes, {
        through: 'usuarios_permissoes',
        as: 'usuarios_permissions',
        foreignKey: 'usuario_id'
      })
    }
  }
  usuarios.init({
    nome: DataTypes.STRING,
    email: DataTypes.STRING,
    senha: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'usuarios',
  });
  return usuarios;
};