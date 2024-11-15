from fastapi import FastAPI
import random

import encoder

app = FastAPI()

file = 'test.py'

lteconder = encoder.LTEncoder(32, file)
    ## Processing File:
f = open(file).read()


# TODO: File selector
# NOTE: This could lead to security issue but I dont give a sh!t
@app.get("/data/{filepath}")
async def root(filepath: str):
    return {"message": filepath}

# TODO: This part should be integrated with LT-code

@app.get("/file/{segment}")
async def get_file_segment(segment: str):
    for block in lteconder._gen_blocks("This is something    iajsodiahsd oaishdo iahsodiaosidh oas odaihsdo iahsod  iaosidh  oiahsodi !sdas asdasd"):
        return block

