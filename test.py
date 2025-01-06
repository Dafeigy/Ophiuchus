from fastapi import FastAPI
import random
from fastapi.responses import StreamingResponse

import encoder

app = FastAPI()

file = 'test.txt'

lteconder = encoder.LTEncoder(32, file)
    ## Processing File:
f = open(file).read()

filestream_generator = lteconder._gen_blocks(f)


# TODO: File selector
# NOTE: This could lead to security issue but I dont give a sh!t
@app.get("/data/{filepath}")
async def root(filepath: str):
    return {"message": filepath}

# TODO: This part should be integrated with LT-code

@app.get("/file/")
async def get_file_segment():
    return next(filestream_generator)

