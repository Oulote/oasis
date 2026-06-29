from django.http import HttpResponseForbidden

class AdminIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            allowed_ips = ['127.0.0.1', '192.168.1.1']
            ip = request.META.get('REMOTE_ADDR')
            if ip not in allowed_ips and ip != '::1':
                return HttpResponseForbidden("Accès interdit")
        return self.get_response(request)