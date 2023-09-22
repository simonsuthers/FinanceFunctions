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


@bp.route(route="DfsTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def DfsTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    credential = DefaultAzureCredential()

    apikey = os.environ["alphavantageapikey"]
    account_url = os.environ["FinanceDfsStorage"]
    file_path = "file03.txt"

    file = DataLakeFileClient(account_url=account_url, 
                              credential=credential, 
                              file_system_name="finance", 
                              file_path=file_path)
    
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    data = json.dumps(data)
    
    file.create_file()
    file.append_data(data, offset=0, length=len(data))
    file.flush_data(len(data))

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    

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
