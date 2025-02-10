from fastapi import FastAPI
#from app.routes import predict, health

app = FastAPI(title="ML FastAPI Service")

#app.include_router(predict.router)
#app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "API de IA en FastAPI está funcionando"}