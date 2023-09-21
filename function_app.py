import azure.functions as func
import logging
import os
import requests
import json


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpTrigger")
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = os.environ["alphavantageapikey"]

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. User name is {username}")
    else:
        return func.HttpResponse(
             f"This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response. User name is {username}",
             status_code=200
        )
    

@app.route(route="BlobTrigger")
@app.blob_output(arg_name="outputblob", path="finance/test.txt", connection="FinanceBlobStorage") 
def BlobTrigger(req: func.HttpRequest, outputblob: func.Out[str]):
    logging.info(f"Python blob trigger function processed blob")

    apikey = os.environ["alphavantageapikey"]

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    data = json.dumps(data)

    outputblob.set(data)
    
    return func.HttpResponse(f"This HTTP triggered function executed successfully. apikey is {apikey}")
