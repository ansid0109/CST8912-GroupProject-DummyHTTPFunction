import json

import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="dummy_http_trigger")
def dummy_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        return func.HttpResponse(
            json.dumps(
                {
                    "message": f"Hello, {name}. This HTTP triggered function executed successfully."
                }
            ),
            status_code=200,
            mimetype="application/json",
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Please pass a name on the query string or in the request body"}),
            status_code=400,
            mimetype="application/json",
        )
