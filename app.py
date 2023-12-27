from fastapi import FastAPI

app = FastAPI(debug=True)

from routers import app