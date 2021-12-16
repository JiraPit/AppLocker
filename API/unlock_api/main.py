from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DETA_PROJECT_ID = 'c08ec7nt'
DETA_API_KEY='c08ec7nt_jZ7xpMmh8u21xoD7WWtLL2SwhjdSa1nf'

#c08ec7nt_jZ7xpMm8u21xoD7WWtLL2SwhjdSa1nf

URL = 'https://database.deta.sh/v1/'+DETA_PROJECT_ID+'/userLockingStatus/items'

@app.get('/getstatus')
async def set_status():
    resp = requests.get(
        url=URL+'/lock_status',
        headers={
            'X-API-Key':DETA_API_KEY,
            'Content-Type': 'application/json'
        },
    )
    return resp.json()["value"]

@app.get('/setstatus/{value}')
async def set_status(value : str):
    resp = requests.put(
        url=URL,
        headers={
            'X-API-Key':DETA_API_KEY,
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            "items" : [
                {
                    "key":"lock_status",
                    "value":value,
                }
            ]
        }
    )
    )
    return resp.json()["processed"]["items"][0]["value"]
