class JWTController:
    @staticmethod
    def configureJWT():
        from main import jwt
        @jwt.user_identity_loader
        def createUserSession(user_id):
            return {
                'user_id': user_id
            }

        @jwt.unauthorized_loader
        def noTokenResponse(msg):
            from .response_helper import responde
            return responde(401,True,msg,{'action': 'LOGIN'})

        @jwt.expired_token_loader
        def expiredToken(msg,callback):
            from .response_helper import responde
            return responde(401,True,'Expired token',{'action': 'REFRESH'})