from sqlalchemy import create_engine
import boto3
import json
import yaml
class ReadYMLFile:
    
    def __init__(self,ymlfilepathwithname):
        '''
        ymlfilepathwithname: it should contains the path with file name
            ex: D:\\Optimeyes\\credentials.yaml
        
        '''
        self.ymlfilepath=ymlfilepathwithname
    
    def read_yml_file(self):
        file=self.ymlfilepath
        with open(file,'r') as f:
            yamlfile=yaml.safe_load(f)
        return yamlfile
    
class MySqlConnectWithoutConfig:
    def __init__(self,secret_name:str,region_name:str,aws_access_key_id:str,aws_secret_access_key:str):
        self.AWS_SECRET_NAME=secret_name
        self.AWS_REGION_SECRET=region_name
        self.AWS_ACCESS_KEY_ID=aws_access_key_id
        self.AWS_SECRET_ACCESS_KEY=aws_secret_access_key
        
    def get_secret(self,secret_name, region_name,aws_access_key_id,aws_secret_access_key):
        # Create a Secrets Manager client
        session = boto3.session.Session(aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,region_name=region_name)
        client = session.client(service_name="secretsmanager", region_name=region_name)
        return client.get_secret_value(SecretId=secret_name)["SecretString"]

    def create_engine_conn(self,db_name):
        secret_value = self.get_secret(self.AWS_SECRET_NAME,self.AWS_REGION_SECRET,self.AWS_ACCESS_KEY_ID, self.AWS_SECRET_ACCESS_KEY)
        if secret_value:
            secret_data = json.loads(secret_value)
            rds_user = secret_data["username"]
            rds_pass = secret_data["password"]
            rds_host = secret_data["host"]
            rds_port = secret_data["port"]
            
            engine = create_engine(
                f"mysql+pymysql://{rds_user}:{rds_pass}@{rds_host}:{rds_port}/{db_name}"
            )
        else:
            raise Exception("RDS Connection Failed")
            engine = None
        return engine
    
    def save_data_to_db(self,dbname,dataframe,tablefilename,ifexists="append"):
        '''
        this function will use dataframe.to_sql function to save the dataframe into database
        
        dbname: database name where the file to be save 
        dataframe: it should be a DataFrame and 
                    there should not be any "id" column consist int the dataframe
        tablefilename: it will consist the name of file for database table in mysql
        ifexists: it define either want to replace the table to append the table
                    by default it is append,if needed can be change to "replace".
        '''
        engineconnect=self.create_engine_conn(dbname)
        start_number = 1 
        dataframe.reset_index(drop=True, inplace=True)
        dataframe.index += start_number
        dataframe.to_sql(name= tablefilename, con=engineconnect, if_exists=ifexists, index=True,index_label='id')
        return f"datafraame sucessfully inserted into the database"
