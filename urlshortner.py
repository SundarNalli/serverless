import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    request_url = req.params.get('url')
    if not request_url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            request_url = req_body.get('url')

    if request_url:
        url = 'https://gotiny.cc/api'
        payload = '{"input":"' + request_url + '"}'
        headers = { "Content-Type": "application/json" }
        x = requests.post(url,payload, headers=headers)

        return func.HttpResponse(x.text)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass an URL in the query string or in the request body for a personalized response.",
             status_code=200
        )
