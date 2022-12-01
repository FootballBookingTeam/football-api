import jwt
from rest_framework.exceptions import AuthenticationFailed


def user_authentication(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('User is not authenticated')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('JWT token expired')
    return payload
