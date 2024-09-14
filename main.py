from fastapi import FastAPI

#Create an instance of the FastAPI app
app = FastAPI()

@app.get("/")
def rot():
    return {"message": "Hello World!"}