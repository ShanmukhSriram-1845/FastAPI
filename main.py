from fastapi import FastAPI
from database import database
app = FastAPI()
@app.get("/")
def welcome():
    return "hello"




@app.get("/S")
def Default(Name:str):
    return Name

@app.post("/")
async def Details(Name: str, Phone_Number: str, Age: str):
    await database.Details.insert_one({"Name":Name,"Phone_number":Phone_Number,"age":Age})
    return "inserted successfully"
@app.get("/Mobile")
async def getName(age:str):
    result= await database.Details.find({"age": age}).to_list()
    for detail in result:
        detail["_id"]=str(detail["_id"])


    return result
@app.patch("/Updation")
async def Update(phone_number:str,Name: str):
    result = await database.Details.update_one({"Phone_number":phone_number},{"$set":{"Name":Name}})
    return result.modified_count