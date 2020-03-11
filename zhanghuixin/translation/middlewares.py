from django.utils.deprecation import MiddlewareMixin


def my_middleware(get_response1):
    print('init 被调用')
    def middleware(request):
        print('before request 被调用')
        response = get_response1(request)
        print('after response 被调用')
        return response
    return middleware

def my_middleware2(get_response):
    print('init2 被调用')
    def middleware(request):
        print('before request 2 被调用')
        response = get_response(request)
        print('after response 2 被调用')
        return response
    return middleware


class OpenIdSessionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__()
        self.get_response = get_response
        print('middleware3 init')

    def process_request(self, request):
        print('middleware3 process request')

    def process_view(self, *args):
        print('middleware3 process_view')

    def process_response(self, request, response):
        print('middleware3 process response')

        return response

