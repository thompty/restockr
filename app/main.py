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
            "app_name": "Restockr",
            "welcome_message": "Welcome to the Restockr Grocery Assistant"
        }
    )

@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={
            "app_name": "Restockr",
            "description": "This program is used for the user to input a scan of a reciept which is then converted to data in a database. "
        }
    )

@app.get("/status")
def status(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="status.html",
        context={
            "app_name": "Restockr",
            "app_running": "App is Running"
        }
    )