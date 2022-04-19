from elasticsearch import Elasticsearch

class es_client:
    """This class connects to the elastic search"""
    def __init__(self):
        self.__ELASTIC_PASSWORD = "<password>"
        self.__es_host="https://localhost:9200"
        self.__es_certificate="http_ca.crt"
        self.__basic_auth=("elastic", self.__ELASTIC_PASSWORD)
        self.es_client=None
        
        
        self.set_es_client()
    def set_es_client(self):
        self.es_client=Elasticsearch(self.__es_host, ca_certs=self.__es_certificate, basic_auth=self.__basic_auth)
                
        
        
        


    
