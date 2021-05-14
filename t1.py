import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    n = req.params.get('n')
    if not n:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            n = req_body.get('n')

    if n:
        data = {'fibonacciNumber': fib(int(n)), 'n': n}
        out = json.dumps(data)
        return func.HttpResponse(out)
    else:
        return func.HttpResponse(
             "No params",
             status_code=200
        )


def fib(n):
    arr = [0, 1]

    for i in range(n-1):
        arr += [arr[-1] + arr[-2]]

    return arr[-1]
