from fastapi import FastAPI

# Declaring the app variable
main = FastAPI()


@main.get("/")
async def root():
    return {"message": "Hello World!"}


# Using a path
@main.post("/login/{id}")
async def login(id: int):
    name = "FirstName"
    last_name = "LastName"
    return {"success": True} if (name == "FirstName" and last_name == "LastName" and id == 2003) else {"success": False}


# Using a path
@main.post("/login/")
async def loginWithQueries(id: int):
    name = "FirstName"
    last_name = "LastName"
    return {"success": True} if (name == "FirstName" and last_name == "LastName" and id == 2003) else {"success": False}
