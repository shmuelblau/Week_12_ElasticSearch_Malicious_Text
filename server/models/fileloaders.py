
import csv
import json



class FileLoader:
    @staticmethod
    def read( file_name) -> list:
        return []

# ------------------------------------------------------------------
class TxtLoader(FileLoader):
    @staticmethod
    def read( file_name) -> list:
        with open(file_name , 'r') as f :
            return list(f.readlines())

# ------------------------------------------------------------------

class CsvLoader(FileLoader):
    
    @staticmethod
    def read( file_name) -> list[dict]:
        data = []
        with open(file_name , newline='', encoding='utf-8') as f :
           reader = csv.DictReader(f)
           data = list(reader)
        
        return data
    
