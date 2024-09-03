from enum import Enum


class Property(object):
    api_name: str
    java_name: str
    cap_java_name: str
    type: str

    def __init__(self, api_name: str, java_name: str, cap_java_name: str, type: str):
        self.api_name = api_name
        self.java_name = java_name
        self.cap_java_name = cap_java_name
        self.type = type


class EnumProperty(object):
    api_name: str
    java_name: str

    def __init__(self, api_name: str, java_name: str):
        self.api_name = api_name
        self.java_name = java_name


class HttpMethod(Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4


class ApiMethod(object):
    name: str
    input: str
    output: str
    method: HttpMethod
    url: str

    def __init__(self, name: str, input: str, output: str, method: HttpMethod, url: str):
        self.name = name
        self.input = input
        self.output = output
        self.method = method
        self.url = url
