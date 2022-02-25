from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from server.models.mymodel import _request
from server.utils.add import add
from server.utils.sub import sub
from server.utils.mul import mul
from server.utils.div import div

app= FastAPI()

@app.post("/fastapi/v1/add")
def get_sum_of_number(item :_request):

    import pdb
    pdb.set_trace()
    payload = jsonable_encoder(item)

    my_sum_var = add(payload.get("var1"), payload.get("var2"))
    
    return ({"Addition" : my_sum_var})

@app.post("/fastapi/v1/sub")
def get_sub_of_number(item :_request):

    payload = jsonable_encoder(item)
    my_sub_var = sub(payload.get("var1"), payload.get("var2"))

    return ({"Subtraction" : my_sub_var})

@app.post("/fastapi/v1/mul")
def get_mul_of_number(item :_request):

    payload = jsonable_encoder(item)
    my_mul_var = mul(payload.get("var1"), payload.get("var2"))

    return ({"Multiplication" : my_mul_var})

@app.post("/fastapi/v1/api")
def get_div_of_number(item :_request):

    payload = jsonable_encoder(item)
    my_div_var = div(payload.get("var1"), payload.get("var2"))

    return ({"Division" : my_div_var})
