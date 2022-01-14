# Basic airflow

This is my combination of airflow, fastapi and dynamodb

Just a simple app with the flow: 
  - is_api_available: check api from fastapi (localhost:8000/user/GiangHoaTran)
  - extracting_user: return information from is_api_available
  - processing_user: extract user using PythonOperator and save information as json file (user_information.json)
  
is_api_available >> extracting_user >> processing_user

-------------------------------------------------------------------
-> Everytime you run airflow command, it will init a workplace named airflow, you can change the workplace's place inside bashrc in order to keep it always be activated whenever you open a new terminal by:\
sudo nano ~/.bashrc\
- then add the line below inside the bashrc\
export AIRFLOW_HOME=/your-destination (Example: export AIRFLOW_HOME=/home/MyCode/airflow)

-> Enter virtual environment whenever you open a new terminal\
source env/bin/activate

-> Run airflow webserver\
airflow webserver (http://localhost:8080/)

-> Run airflow scheduler\
airflowl scheduler

-> Run uvicorn for fastapi\
uvicorn app.main:app --reload (http://localhost:8000/)

-> Uncomment create table function in app/db/utils.py to create a TestTable in DynamoDB then run below command\
python app/db/utils.py

-> Create a user at http://localhost:8000/docs/, this will return an api at http://localhost:8000/users/your-user \
Example: http://localhost:8000/users/VuNgocLong

-> You should login first with username/password is admin/admin in order to get JWT, enter it in HTTPBearer to use API call !!!

-> Inside dags/my_dag, change end_point in each operator user/GiangHoaTran into your user you created

-> If you want to test a task inside my_dag (example: is_api_available)\
airflow tasks test my_dag is_api_available 2022-01-01
