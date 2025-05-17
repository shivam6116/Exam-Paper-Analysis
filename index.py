from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pdf2image import convert_from_bytes

import uvicorn
import numpy as np
from src.util.ocr_function import ocr_easyocr, get_extracted_text

from src import create_app
app = create_app()


if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0", port=8000)
