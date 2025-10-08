import os
from fastapi import FastAPI ,status
from main import DATA_FILE ,logger

app=FastAPI()

@app.get("/healthz", status_code=status.HTTP_200_OK)
def health_check():
    """
    Checks the service health and verifies the existence of the data file.
    Always returns 200 OK if the service is running, with detailed status.
    """
    # Check if the data file exists on the file system
    file_exists = os.path.exists(DATA_FILE)
    
    status_detail = {
        "status": "OK",
        "service": "Book CRUD API",
        "data_file_status": "Available" if file_exists else "Missing (Check deployment volume)",
    }
    
    logger.info(f"Health check performed. Data file status: {status_detail['data_file_status']}")
    return status_detail