from fastapi import FastAPI

app = FastAPI()

# Create an endpoint - an endpoint is the point of entry in a communication between an API and a server
# base url will be local host since we are not deploying anyway

@app.get("/")
def home ():
    return {"Data" : "Testing"}

@app.get("/about")
def about ():
    return {"Data": "about"}