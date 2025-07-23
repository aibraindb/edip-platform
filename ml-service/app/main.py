from fastapi import FastAPI
from app.kafka_consumer import start_kafka_listener

app = FastAPI()

@app.get("/")
def root():
    return {"message": "EDIP ML Service Running"}

@app.on_event("startup")
async def startup_event():
    print("🚀 Starting Kafka listener...")
    start_kafka_listener()
