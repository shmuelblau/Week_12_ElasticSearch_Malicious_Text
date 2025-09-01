from typing import Callable
from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from models.logger import Logger
from models.QueryBuilder import QueryBuilder
class ElasticDAL:
# ----------------------------------------------------------------------------

    def __init__(self , elastic_conn:Elasticsearch) -> None:
       self.conn:Elasticsearch = elastic_conn

# ----------------------------------------------------------------------------

    @property
    def get_conn(self) -> Elasticsearch:
        return self.conn
    
# ----------------------------------------------------------------------------
    @Logger
    def get_all_from_index(self , index)-> list:
        result = self.search( index ,{"query": {"match_all": {}}})
        return result
# ----------------------------------------------------------------------------

    @Logger
    def search(self , index , query)-> list:
        result = self.conn.search(index=index , body= query)
        return result['hits']['hits']
# ----------------------------------------------------------------------------

    @Logger
    def insert_bulk(self , index , data:list):
        bulk(self.conn, data)

# ----------------------------------------------------------------------------

    @Logger(log_start=False)
    def insert(self , index , data:dict) -> ObjectApiResponse:
        result = self.conn.index(index= index ,document= data)
        return result
# ----------------------------------------------------------------------------

    @Logger
    def set_mapping_index(self , index:str , mapping:dict)-> ObjectApiResponse:

        result = self.conn.indices.create(index=index , mappings=mapping)
        return result
# ----------------------------------------------------------------------------
    @Logger
    def add_to_mapping(self , index:str , mapping:dict)-> ObjectApiResponse:
        mapp = QueryBuilder.get_mapping(mapping)
        result = self.conn.indices.put_mapping(index=index , body=mapp)
        return result
# ----------------------------------------------------------------------------
    def delete_by_query( self ,index , query )-> ObjectApiResponse:
        result = self.conn.delete_by_query(index=index, body=query)
        return result

    # @Logger
    # def add_field_by_func(self , index , field_name ,  field_type  , func: Callable[[str], str | list[str]]):
    #     self.add_to_mapping(index ,{field_name:field_type})
    #     data = self.get_all_from_index(index)



        

