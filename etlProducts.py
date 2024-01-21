import requests #interact with APIs
import pandas as pd #data manipulation
from sqlalchemy import create_engine 
import configparser

def etl_process():
    # Load my credentials from my config
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Create postgres engine
    postgres_config = config['postgres']

    engine = create_engine(
        f"postgresql://{postgres_config['user']}:{postgres_config['password']}@{postgres_config['host']}:{postgres_config['port']}/{postgres_config['database']}"
    )

    # Northwind API request for order
    url = 'https://demodata.grapecity.com/northwind/api/v1/Products'
    response = requests.get(url)
    data = response.json()

    # Load data into postgres
    df = pd.json_normalize(data)
    df.to_sql('product_raw', engine, if_exists= 'replace', index=False)
    engine.dispose()

etl_process()