from sqlalchemy import create_engine
import boto3
import json
import yaml
class ReadYMLFile:   
    def __init__(self,ymlfilepathwithname):
        '''
        ymlfilepathwithname: it should contains the path with file name        
        '''
        self.ymlfilepath=ymlfilepathwithname
    
    def read_yml_file(self):
        filename=self.ymlfilepath
        with open(filename,'r') as f:
            yamlfile=yaml.safe_load(f)
        return yamlfile
    