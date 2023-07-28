'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class usuario_role extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  usuario_role.init({
    usuario_id: DataTypes.UUID,
    role_id: DataTypes.UUID
  }, {
    sequelize,
    freezeTableName: true,
    modelName: 'usuario_role',
  });
  return usuario_role;
};