from fastapi import FastAPI
from api.endpoints import items

# Create an instance of the FastAPI class
app = FastAPI()


@app.get("/")
async def root():
    """
    Root endpoint which returns a welcome message.

    Returns:
        dict: A dictionary with a key 'message' containing a greeting string.
    """
    return {"message": "Hello, World!"}


# Include the item endpoints from the items module
app.include_router(items.router)

# Uncomment the following lines to run the application directly using Uvicorn
# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
