from fastapi import FastAPI 

app = FastAPI(
    title="Healix API",
    description="API for Healix, a health management system",   
    version="0.1.0",
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Healix API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/about")
async def about():
    return {"project": "Healix", "description": "A health management system API", "version": "0.1.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)