## PARA RODAR O PROJETO

CRIE UM VIRTUAL ENVIRONMENT COM QUALQUER UM DA SUA ESCOLHA
Os comandos que eu utilizo: 
virtualenv -p python3.9 env
source env/bin/activate
pip install -r requirements.txt


## PARA RODAR O DOCKER COMPOSE
docker-compose up -d
ou
docker-compose -f docker-compose.yml up -d

### Se quiser rodar separado cada máquina do docker
docker-compose -f docker-compose.yml up kafka-1 (ou os outros) -d
