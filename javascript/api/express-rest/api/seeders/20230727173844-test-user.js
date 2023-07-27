'use strict';
const { v4: uuidv4 } = require('uuid');
const { hash } = require('bcrypt');

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    const password = 'test';
    const senhaHash = await hash(password, 8);
    await queryInterface.bulkInsert('usuarios', [
      {
        id: uuidv4(),
        nome: 'test',
        email: 'test@example.com',
        senha: senhaHash,
        createdAt: new Date(),
        updatedAt: new Date()
      }
    ]);
  },

  async down (queryInterface, Sequelize) {
    await queryInterface.bulkDelete('usuarios', null, {});
  }
};
