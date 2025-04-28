def role_middleware(*roles):
    def middleware(req, res, next):
        if not req.user:
            return res.status(401).json({'message': 'Unauthorized'})
        if not any(role in req.user['roles'] for role in roles):
            return res.status(403).json({'message': 'Forbidden'})
        next()
    return middleware

