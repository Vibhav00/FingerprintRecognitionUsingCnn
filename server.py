import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS,cross_origin
import pickle
import json
from keras.models import load_model 
from PIL import Image
from numpy import asarray
from numpy import zeros, newaxis
 

app = Flask(__name__)
model = load_model("model.h5") 
CORS(app)
CORS(app, resources={r"/pre": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


def downsample_image(img):
    img = Image.fromarray(img.astype('uint8'), 'L')
    img = img.resize((103,96), Image.LANCZOS)
    return np.array(img)


  
@app.route('/pre',methods=['POST'])
def ab():
    try:
        if request.method=='POST':
            image=request.files['image']
            image_name=image.filename
            PIL_img = Image.open(image).convert('L')
            img_numpy = np.array(PIL_img,'uint8')
            print(img_numpy.shape)
            arr=np.array([img_numpy])
            print(arr.shape)

            # img=downsample_image(img_numpy)
            # print(img.shape)
            y_predicted = model.predict(arr)
            y_predicted_labels = [np.argmax(i) for i in y_predicted]
            return {"response":str(y_predicted_labels[0])+""}
            # return {"error":"select you image file"}
        else:
                return {"error":"select you image file"}
    except Exception as e:
        return {"error":str(e)}

if __name__ == "__main__":
    app.run(debug=True)



# //http://127.0.0.1:5000/pre    form data img image