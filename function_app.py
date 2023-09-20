import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpTrigger")
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

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
    

@app.route(route="BlobTrigger")
@app.blob_output(arg_name="outputblob", path="finance/test.txt", connection="AzureBlobStorage") 
def BlobTrigger(req: func.HttpRequest, outputblob: func.Out[str]):
    logging.info(f"Python blob trigger function processed blob")

    clear_text = "hello"
    
    outputblob.set(clear_text)
    
    return func.HttpResponse(f"This HTTP triggered function executed successfully.")
