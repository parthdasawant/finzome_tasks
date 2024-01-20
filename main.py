import io
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from task1 import calculate_volatilities  # Import the function from Task 1

app = FastAPI()


@app.post("/calculate_volatilities/")
async def calculate_volatilities_endpoint(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        csv_text = contents.decode('utf-8')
        data = io.StringIO(csv_text)
        (daily_volatility, annualized_volatility) = calculate_volatilities(data)

        return JSONResponse({
            "daily_volatility": daily_volatility,
            "annualized_volatility": annualized_volatility
        })

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
