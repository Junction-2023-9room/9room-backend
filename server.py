import openai
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import company
from routers import progress
from routers import waste

# Create the FastAPI application
app = FastAPI()

# Initialize the OpenAI ChatGPT model
openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-3.5-turbo"

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(company.router)
app.include_router(progress.router)
app.include_router(waste.router)


@app.get("/")
def read_root():
    return {"Junction?": "9room!"}
