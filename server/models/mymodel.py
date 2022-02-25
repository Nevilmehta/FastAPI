from typing import List
from pydantic import BaseModel

class request(BaseModel):
    oper:List[str]
    var1:int
    var2:int
    