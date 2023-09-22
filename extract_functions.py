import logging 
import os
import requests
import json
from azure.storage.filedatalake import DataLakeServiceClient, DataLakeFileClient
from azure.identity import DefaultAzureCredential
import azure.functions as func 

from shared_code import my_helper_function

bp = func.Blueprint() 

@bp.route(route="BlobTrigger")
@bp.blob_output(arg_name="outputblob", path="test.txt", connection="FinanceBlobStorage") 
def BlobTrigger(req: func.HttpRequest, outputblob: func.Out[str]):
    logging.info(f"Python blob trigger function processed blob")

    apikey = os.environ["alphavantageapikey"]
    name = "finance/test.txt"

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    data = json.dumps(data)

    outputblob.set(data)
    
    return func.HttpResponse(f"This HTTP triggered function executed successfully.")


@bp.route(route="ticker", auth_level=func.AuthLevel.ANONYMOUS)
def GetTicker(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #ticker = req.route_params.get('ticker')

    ticker = req.params.get('ticker')
    if not ticker:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ticker = req_body.get('ticker')

    if not ticker:
        ticker = "IBM"

    credential = DefaultAzureCredential()

    apikey = os.environ["alphavantageapikey"]
    account_url = os.environ["FinanceDfsStorage"]
    file_path = f"{ticker}.txt"

    file = DataLakeFileClient(account_url=account_url, 
                              credential=credential, 
                              file_system_name="finance", 
                              file_path=file_path)
    
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    data = json.dumps(data)
    
    file.create_file()
    file.append_data(data, offset=0, length=len(data))
    file.flush_data(len(data))

    return func.HttpResponse(f"Hello, {ticker}. This HTTP triggered function executed successfully.", status_code=200)

    

@bp.function_name(name="my_second_function")
@bp.route(route="hello")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Executing my_second_function.')

    initial_value: int = int(req.params.get('value'))
    doubled_value: int = my_helper_function.double(initial_value)

    return func.HttpResponse(
        body=f"{initial_value} * 2 = {doubled_value}",
        status_code=200
    )
