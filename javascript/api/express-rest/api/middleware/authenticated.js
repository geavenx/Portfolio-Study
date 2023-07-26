const { verify, decode } = require('jsonwebtoken');
const jsonSecret = require('../config/jsonSecret');

module.exports = async (req, res, next) => {
    const token = req.headers.authorization

    if (!token) {
        return res.status(401).send("Token not given")
    }

    const [, accessToken] = token.split(" ");

    try {
        verify(accessToken, jsonSecret.secret);

        const { id, email } = await decode(accessToken);
        
        req.userId = id
        req.userEmail = email
        
        return next();

    } catch (err) {
        res.status(401).send("User not authorized");
    }
}