from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Token

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return None
        
        try:
            token_value = token.split()[1]
            token_obj = Token.objects.get(token=token_value)
            return (token_obj.user, None)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        return None
