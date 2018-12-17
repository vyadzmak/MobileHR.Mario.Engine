from enum import Enum

#http request types
class RequestTypesCollection(Enum):
    GET_ALL = 0
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
    OPTIONS = 5


#colletion of request types
class RequestAnswersCollection(Enum):
    JSON =0
    CSV = 1
    XML =2
    FILE =4
    URL = 5


#collection of data sources
class DataSourcesCollection(Enum):
    HTTP =0
    FTP =1
    LOCAL = 2
