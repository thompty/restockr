from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

#This line tells FastAPI which dir the templates are located
templates = Jinja2Templates(directory="app/templates")

#response_class=HTMLResponse tells us its a web page not a JSON
@app.get("/", response_class=HTMLResponse)
#Definition for home page routed at / while also including HTTP request information
def home(request: Request):
    #Template for home.html file which loads the html file, renders it, and sends it to the browser
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        #Data passed from Python into the HTML template
        context={
            "app_name": "Restockr Development",
            "welcome_message": "Welcome to the Restockr Grocery Assistant"
        }
    )

@app.get("/about")
def about():
    return {"description": "Restockr is a grocery purchase tracking application"}

@app.get("/status")
def status():
    return {"status": "Restockr is Running"}