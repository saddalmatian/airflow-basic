# airflow-fastapi-dynamodb-basic

This is my combination of airflow, fastapi and dynamodb

Just a simple app with the flow: 
  - is_api_available: check api from fastapi (localhost:8000/user/GiangHoaTran)
  - extracting_user: return information from is_api_available
  - processing_user: extract user using PythonOperator and save information into csv file (test.csv)
  
is_api_available >> extracting_user >> processing_user

-------------------------------------------------------------------
-> Enter virtual environment whenever you open a new terminal\
source env/bin/activate

-> Run airflow webserver\
airflow webserver (http://localhost:8080/)

-> Run airflow scheduler\
airflowl scheduler

-> Run uvicorn for fastapi\
uvicorn app.main:app --reload (http://localhost:8000/)

-> If you want to test a task inside my_dag (example: is_api_available)\
airflow tasks test my_dag is_api_available 2022-01-01
