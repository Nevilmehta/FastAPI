from fastapi import FastAPI
from server.models.mymodel import request
from fastapi.encoders import jsonable_encoder
from server.utils.fun import func

app=FastAPI()

@app.post("/fastapi/v1/request")
def output(item:request):

    payload=jsonable_encoder(item)
    output_final=func(payload.get("var1"), payload.get("var2"), payload.get("oper"))
    return ({"final": output_final})
