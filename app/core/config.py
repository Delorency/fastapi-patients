import os

from pydantic_settings import BaseSettings

from dotenv import load_dotenv


load_dotenv()

class ProjectConfig(BaseSettings):
	project_name:str = os.getenv('PROJECT_NAME', 'Patients managment')
	cfg:str
	for cfg in [project_name]:
		if cfg is None:
			raise Exception('Parsing project config error')


class ServerConfig(BaseSettings):
	host:str = os.getenv('HOST', 'localhost')
	port:int = os.getenv('PORT', 8080)


class DBConfig(BaseSettings):
	db_host:str = os.getenv('DB_HOST')
	db_port:str = os.getenv('DB_PORT')
	db_name:str = os.getenv('DB_NAME')
	db_user:str = os.getenv('DB_USER')
	db_pass:str = os.getenv('DB_PASS')
	cfg:str
	for cfg in [db_host, db_port, db_name, db_user, db_pass]:
		if cfg is None:
			raise Exception('Parsing db config error')

	database_uri_format:str = "postgresql://{user}:{password}@{host}:{port}/{name}"
	database_uri:str = database_uri_format.format(
		user=db_user,
		password=db_pass,
		host=db_host,
		port=db_port,
		name=db_name,
	)

class APIConfig(BaseSettings):
	page:int = os.getenv('PAGE', 1)
	limit:int = os.getenv('LIMIT', 10)
	

class Configs(BaseSettings):
	projectcfg:ProjectConfig = ProjectConfig()
	servercfg:ServerConfig = ServerConfig()
	dbcfg:DBConfig = DBConfig()
	apicfg:APIConfig = APIConfig()