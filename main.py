from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your frontend's origin
origins = [
    "http://my-frontend-aws-demo-vue.s3-website-us-west-2.amazonaws.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}

