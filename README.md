# poc_dbt_dremio_airflow



Para rodar o Docker Compose:

Criar as pastas:
mkdir ./src/dags ./src/scripts ./src/spark

Subir a Imagem com o comando:
docker-compose up -d

Criar o usuário airflow:
docker-compose run airflow-webserver airflow users create --role Admin --username airflow --email airflow@example.com --firstname airflow --lastname airflow --password airflow