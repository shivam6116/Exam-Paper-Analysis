from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pdf2image import convert_from_bytes
import easyocr
import uvicorn
import numpy as np

app = FastAPI()
reader = easyocr.Reader(['en'])  # Load once at startup

POPPLER_PATH = r"C:\\Users\\HP\\OneDrive\\Desktop\\UN\\poppler-24.08.0\\Library\\bin"  # Adjust path based on your machine

@app.post("/ocr-pdf-easyocr/")
async def ocr_pdf_easyocr(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        pdf_bytes = await file.read()
        images = convert_from_bytes(pdf_bytes, poppler_path=POPPLER_PATH)
        print()
        results = []
        for img in images:
            img_np = np.array(img)  # Convert PIL image to NumPy array
            text = " ".join([detection[1] for detection in reader.readtext(img_np)])
            print(text)
            results.append(text)

        return JSONResponse(content={"text": results, "pages": len(results)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0", port=8000)
