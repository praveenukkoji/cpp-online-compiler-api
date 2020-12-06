from execute.utils import getCppOutput, getCppOutput1, getPythonOutput, getPythonOutput1
from execute.constants import cpp, python


class OnlineCompiler:

    def __init__(self, request):
        self.request = request

    def getOutput(self):
        payload = ""
        message = ""
        try:
            sourcecode = self.request.get('sourcecode', None)
            input_ = self.request.get('input', None)
            if input_ == "":
                input_ = None
            filetype = self.request.get('filetype', None)

            if not (sourcecode and filetype):
                return "", "Missing Parameters"

            if input_:
                if filetype == cpp:
                    payload, message = getCppOutput(sourcecode, input_)
                elif filetype == python:
                    payload, message = getPythonOutput(sourcecode, input_)
            else:
                if filetype == cpp:
                    payload, message = getCppOutput1(sourcecode)
                elif filetype == python:
                    payload, message = getPythonOutput1(sourcecode)
        except Exception as e:
            print(e)

        return payload, message
