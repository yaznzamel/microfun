# Endpoints for handling functions (upload, list, delete)
from fastapi import APIRouter , UploadFile , HTTPException
import os 

router = APIRouter()



@router.post("/functions")
async def upload_functions(file : UploadFile):

    """
    Upload a new function to microfun service
    """