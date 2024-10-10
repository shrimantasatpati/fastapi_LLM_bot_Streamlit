from fastapi import FastAPI, Request, Form, Response
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
# FastAPI object, interacting with HTML form
from fastapi.templating import Jinja2Templates
#JinjaTemplates -> it is a language for interacting with the HTML ( for templating, rendering HTML template)
from fastapi.encoders import jsonable_encoder
# Converts data to a JSON-compatible format.
import uvicorn
#uvicorn -> application server for the FastAPI
# ASGI server for running the FastAPI app.
import json
import os
from dotenv import load_dotenv
from QASystem.retrieval_and_generation import get_result

app = FastAPI() #FastAPI Instance
# Enable CORS
# Added CORSMiddleware to the FastAPI app to allow cross-origin requests.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify your Streamlit app URL)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# initializes Jinja2 templates, specifying the directory where HTML templates are stored. 
templates = Jinja2Templates(directory = "templates")

#Routing of FastAPI

@app.get("/") #home route
# The index function handles GET requests to this route, returning the index.html template with the request context.
async def index(request: Request): #request is parameter
    return templates.TemplateResponse("index.html", {"request": request})
#getting the request, and giving the response as a template
#from browser, from the url the request is coming to this particular method

#url
'''Defines a POST route to handle form submissions. It takes a question from the form, processes it using get_result, and returns the answer as a JSON response.'''

@app.post("/get_answer")
async def get_answer(request: Request, question: str = Form(...)):
    print(f"Received question: {question}")
    answer = get_result(question)
    response_data = jsonable_encoder({"answer": answer})
    return Response(content=json.dumps(response_data), media_type="application/json")
    
if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8001,reload=True)

# Access URL: Use http://localhost:8001/docs instead of http://0.0.0.0:8001/docs.
# Check Server Status: Ensure the server is running without errors.