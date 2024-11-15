from flask import Flask,Response
import encoder
import sampler
import json
app = Flask(__name__)


# @app.route('/')
# def index_hello():
#     return "Nothing"

data_source = "hello woroksdja osiu ahsdiuahsoiduhaksj basidhal hjklasdhklja jklh"

lteconder = encoder.LTEncoder(32, data_source)
data_stream_generator = lteconder._gen_blocks(data_source)

@app.route("/")
def update_qrcode():
    
    # temp = next(lteconder._gen_blocks("hello woroksdja osiu ahsdiuahsoiduhaksj basidhal hjklasdhklja jklh"))
    # return json.loads(temp)
    return next(data_stream_generator)



if __name__ == '__main__':
    app.run()

