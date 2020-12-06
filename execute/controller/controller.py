from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from execute.implementation.implementation import OnlineCompiler
import json


class ExecuteIde(GenericAPIView):
    def post(self, request, **kwargs):
        response = {'status': 200, 'payload': "", 'message': "", 'error': ""}
        try:
            request = json.load(request)

            online_compiler_obj = OnlineCompiler(request)
            payload, message = online_compiler_obj.getOutput()

            if payload:
                response['payload'] = payload
            response['message'] = message

        except Exception as e:
            print(e)
            response['message'] = "Some error occurred."
            response['error'] = e

        return JsonResponse(response)
