
import pprint
from typing import Callable
from elasticsearch.helpers import bulk
class QueryBuilder:
    
    mapping:dict[str , dict] = {"properties":{}}

    molty_query: dict ={ "query": {"bool": {}}}
# ----------------------------------------------------------------------------
    
    @staticmethod
    def get_mapping(data:dict):
        result = QueryBuilder.mapping
        for name , type in data.items():
            result["properties"][name] = {"type" : type}
        return result
# ----------------------------------------------------------------------------

    
    # @staticmethod
    # def get_match_query(data:dict):
    #     result = QueryBuilder.mapping
    #     for name , type in data.items():
    #         result["properties"][name] = {"type" : type}
    #     return result
# ----------------------------------------------------------------------------

    @staticmethod
    def build_bulk(index , data:list[dict]) -> list[dict]:
        result = []
       
        result = list([{"_index": index, "_source": i} for i in data]
)
        return result
    
# ----------------------------------------------------------------------------
   

    @staticmethod
    def build_update_bulk_by_func(index ,field_name ,data:dict , func: Callable[[str], str | list[str]])-> list:
        result = list([{'_op_type': 'update', '_index': index, '_id': i['_id'] , 'doc': {field_name: func(i["text"])}} for i in data])
        
        return result
    

    # @staticmethod
    # def build_delete_bulk_by_id():
    #      result = list([{'_op_type': 'update', '_index': index, '_id': data['_id'] , 'doc': {field_name: func(data["text"])}}])
        
    #     return result

    # @staticmethod
    
#         "properties": {
#             "title": {"type": "text"},
#             "content": {"type": "text"},
#             "tags": {"type": "keyword"},
#             "publish_date": {"type": "date"}
#         


# data = QueryBuilder.build_bulk("dddd" ,[{"title" : "text" , "content": "text", "tags": "keyword", } , {"title" : "text" , "content": "text", "tags": "keyword", }])
# print(data)