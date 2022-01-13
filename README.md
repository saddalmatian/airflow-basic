# airflow-fastapi-dynamodb-basic

This is my combination of airflow, fastapi and dynamodb

Just a simple app with the flow: 
  - is_api_available: check api from fastapi (localhost:8000/user/GiangHoaTran)
  - extracting_user: return information from is_api_available
  - processing_user: extract user using PythonOperator and save information into csv file (test.csv)
  
