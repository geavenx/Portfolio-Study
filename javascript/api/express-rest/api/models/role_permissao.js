'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class role_permissao extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  role_permissao.init({
    role_id: DataTypes.UUID,
    permissao_id: DataTypes.UUID
  }, {
    sequelize,
    freezeTableName: true,
    modelName: 'role_permissao',
  });
  return role_permissao;
};