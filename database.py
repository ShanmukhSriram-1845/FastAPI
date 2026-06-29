from motor.motor_asyncio import AsyncIOMotorClient

mongourl="mongodb+srv://ssriram1103:Shanmukh1234@cluster0.io5l4.mongodb.net/?appName=Cluster0"

client = AsyncIOMotorClient(mongourl)

database = client["Naruto"]