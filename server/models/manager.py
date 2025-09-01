from models.fileloaders import CsvLoader , TxtLoader, FileLoader
from typing import List, Dict 
from models.logger import Logger
class Manager:

    def __init__(self , weapons_file , tweets_file) -> None:
        self._load_files( weapons_file , tweets_file)
        

    @Logger
    def _load_files(self  , weapons_file , tweets_file):
        self.weapons: List[str] = TxtLoader.read(weapons_file)
        self.tweets: List[Dict] =  CsvLoader.read(tweets_file)


        

    def start_operation(self):
        
        pass
