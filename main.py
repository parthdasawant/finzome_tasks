import io
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
from task1 import calculate_volatilities  # Import the function from Task 1

app = FastAPI()

@app.post("/calculate_volatilities/")
async def calculate_volatilities_endpoint(file: UploadFile = File(...)):
    """
    Calculates daily and annualized volatility from a CSV file.

    Parameters:
    - file (UploadFile): The CSV file to be processed.

    Returns:
    - JSONResponse: A JSON object containing the daily and annualized volatilities.
    """

    try:
        contents = await file.read()
        print(contents)
        csv_text = contents.decode('utf-8')

        data = io.StringIO(csv_text)
        # data = pd.read_csv('my_file.csv')
        (daily_volatility, annualized_volatility) = calculate_volatilities(data)

        return JSONResponse({
            "daily_volatility": daily_volatility,
            "annualized_volatility": annualized_volatility
        })

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)  # Handle errors gracefully

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)