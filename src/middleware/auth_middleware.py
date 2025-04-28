def auth_middleware(req, res, next):
    """
    Middleware to check if the user is authenticated.
    """
    if not req.session.get('user'):
        return res.status(401).json({'message': 'Unauthorized'})
    next()