from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from surya.ocr import run_ocr
from surya.model.recognition.model import load_model
from surya.model.recognition.processor import load_processor
from pdf2image import convert_from_bytes
import io

app = FastAPI()

# Load models once at startup
model = load_model()
processor = load_processor()

@app.post("/ocr-pdf/")
async def ocr_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        
        pdf_bytes = await file.read()
        images = convert_from_bytes(pdf_bytes)

        
        results = []
        for img in images:
            predictions = run_ocr([img], model, processor)
            results.append(predictions[0].text)

        return JSONResponse({"text": results, "pages": len(results)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))