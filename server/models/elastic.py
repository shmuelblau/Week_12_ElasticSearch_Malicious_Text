from elasticsearch import Elasticsearch
from logger import Logger
class Elastic():
    
  
    def __init__(self , host , port = 9200) -> None:
        self.conn: Elasticsearch = self._set_conn( host , port = 9200)
        
    
    
    @Logger
    def _set_conn(self , host , port = 9200):
        self.conn: Elasticsearch = Elasticsearch(f'http://{host}:{port}')
        self.conn.ping()
        return self.conn

    
    @property
    def get_conn(self) -> Elasticsearch:
        return self.conn

