'''Routes are in this'''
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pdf2image import convert_from_bytes


import numpy as np
from src.util.ocr_function import ocr_easyocr, get_extracted_text
 
pilot = APIRouter()



POPPLER_PATH = r"C:\\Users\\HP\\OneDrive\\Desktop\\UN\\poppler-24.08.0\\Library\\bin" 

@pilot.post("/ocr-pdf-easyocr/")
async def ocr_pdf_easyocr(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        pdf_bytes = await file.read()
        images = convert_from_bytes(pdf_bytes, poppler_path=POPPLER_PATH)
        
        # page_text =ocr_easyocr(images)
        page_text =get_extracted_text()  # Only for testing

        return JSONResponse(content={"text": page_text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@pilot.post("/analyze")
async def analyze_extracted_text():
    try:

        page_text =get_extracted_text()  # Only for testing

        return JSONResponse(content={"text": page_text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
