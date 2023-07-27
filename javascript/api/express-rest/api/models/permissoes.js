'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class permissoes extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      permissoes.belongsToMany(models.usuarios, {
        through: models.usuario_permissao,
        as: 'permissao_do_usuario',
        foreignKey: 'permissao_id'
      });
        permissoes.belongsToMany(models.roles, {
        through: models.role_permissao,
        as:'permissao_da_role',
        foreignKey: 'permissao_id'
      });
    }
  }
  permissoes.init({
    nome: DataTypes.STRING,
    descricao: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'permissoes',
  });
  return permissoes;
};