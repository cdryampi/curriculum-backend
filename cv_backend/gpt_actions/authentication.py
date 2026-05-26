from rest_framework.authentication import TokenAuthentication

class BearerTokenAuthentication(TokenAuthentication):
    """
    Custom Token Authentication class that accepts the 'Bearer' keyword
    instead of the default 'Token' keyword, making it fully compatible
    with ChatGPT's standard GPT Actions API Key authorization.
    """
    keyword = 'Bearer'
