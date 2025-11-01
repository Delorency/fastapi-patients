## fastapi-patients  
Service for managing patients and doctors  

### Project description   
The service includes crud functionality for patients and doctors. It allows you   
to assign doctors to patients. It can calculate a patient's BMR using two formulas.   
There's also a webhook for obtaining BMI for each patient.   

### How run service?   
change the corresponding settings in the following files   
```bash
    ./.env
    ./.env_docker
```
#### By docker-compose
then run it in the root of the project     
```bash
    docker compose --env-file=./.env --env-file=./.env_docker up -d
```
or   
```bash
    make docker
```
the service will be on localhost:${DOCKER_HOST_PORT}       
swagger - localhost:${DOCKER_HOST_PORT}/docs   

#### In cmd   
if you want ot run the service in cmd, you need to install all necessary dependencies    
in your local machine. There are many ways to approach this.   

##### via pipenv   
```bash
    pipenv shell && pipenv install -r requirements.txt && python start.py
```
##### via poetry   
```bash
    poetry install && poetry shell && python start.py
```
##### other    
Use requirements.txt   


the service will be on localhost:${PORT}    
swagger - localhost:${PORT}/docs   