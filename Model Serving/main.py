# import libraries
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import load_model

# fastAPI instance
app = FastAPI()

# request body and type of attribute
class request_body(BaseModel):
	text : str

# load saved model
model, label_list = load_model.load()

# endpoint 
@app.post('/predict')
def predict(data : request_body):
	# prediction
	probabilities = model.predict([[
			data.text
	    ]])
    	# get index of highest probability    
	index = np.argmax(probabilities[0])
	
    	# return the result
	return { 'class' : label_list[index],
            'probability' :  probabilities[0][index]}