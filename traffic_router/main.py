import os
import json
from sqlite3 import adapt
import requests

from fastapi import FastAPI, Query, Request, HTTPException, Body
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Service Info
with open(os.path.join(os.path.dirname(os.getcwd()), 'info.json'), 'r') as jf:
    app_info = json.load(jf)

app = FastAPI(
    title=app_info['service_name'],
    description=app_info['description'],
    version=app_info['version'],
)

# Setting up CORS and who can access the API
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(event_router)
# app.include_router(venue_router)
# app.include_router(event_html_router)
# app.include_router(explicit_html_router)
# app.include_router(clean_html_router)
# app.include_router(venue_html_router)



# @app.on_event("startup")
# async def startup_event():
#     db = DatabaseHandler()
#     db.create_tables()
#     context = ContextSingleton()
#     context.database = db
#     context.logger = init_logger()


# # Root
# @app.get('/', status_code=200)
# async def root(request: Request):
#     return {'Hello': 'WORLD!'}

# Root
@app.get('/{extended_path}', status_code=200)
async def root(request: Request, extended_path: str):
    print('ROOT')
    print(extended_path)

    # from requests.adapters import HTTPAdapter
    # from urllib3.util.retry import Retry
    # session = requests.Session()
    # retry = Retry(connect=3, backoff_factor=0.5)
    # adapter = HTTPAdapter(max_retries=retry)
    # session.mount('http://', adapter)
    # session.get('http://localhost:8205/')


    resp = requests.get('http://0.0.0.0:8205/')
    # resp = requests.get('http://localhost:8205/')
    print(f"RESP: {resp}")
    print(f"RESP: {resp.json()}")
    return resp



    # context.logger.debug('GET on /')
    # context.logger.debug(f"REQUEST STUFF")
    # header_details = RestHeaders(request=request)
    # if header_details.response_type == ResponseTypes.HTML:
    #     project_page = project_base_page()
    #     return HTMLResponse(content=project_page)
    # elif header_details.response_type == ResponseTypes.JSON:
    #     return {'Hello': 'WORLD!'}
    return {'Hello': 'WORLD!'}

# endpoint_prefix
# container port
# assocaited ports
# sql specific ports




