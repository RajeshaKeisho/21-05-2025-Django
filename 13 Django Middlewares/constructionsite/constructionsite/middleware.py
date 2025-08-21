from django.http import HttpResponse
from django.conf import settings
import logging

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path != '/under_construction/' and settings.SITE_UNDER_CONSTRUCTION:
            return HttpResponse("Site Under Construction. Please Check Back Later.")
        
        response = self.get_response(request)
        return response
    

class FooterAppendMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 'text/html' in response.get("Content-Type", ''):
            footer_message = "<footer><p>Powered by Django</p></footer>"
            content = response.content.decode('utf-8')

            content = content.replace("<body>", f"{footer_message}</body>")
            response.content = content.encode('utf-8')
        return response
    
logger = logging.getLogger(__name__)
class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except ValueError as e:
            logger.error(f"Value Error Occurred: {e}")
            return HttpResponse("A Value Error Occurred. Please check your input.", status=400)
        except Exception as e:
            logger.error(f"An Unexpected Error Occurred. {e}")
            return HttpResponse("An Unexpected Error Occurred. Please Try Again Later ", staus=500)
    
