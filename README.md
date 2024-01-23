# Project Name

Calculate the Daily Volatility and annualized volatility for the dataset in Python.

## Overview

```bash
.
├── main.py (for Task 2 solution)
├── NIFTY 50-22-01-2023-to-22-01-2024.csv
├── requirements.txt
└── task1.py (for Task 1 solution)

```

## Prerequisites

Make sure you have the following installed before setting up the project:

- Python (version 3.11.3)
- other dependencies are mentioned in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/parthdasawant/finzome_tasks.git
    ```

2. Navigate to the project directory:

    ```bash
    cd finzome_tasks
    ```

3. Set up a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Explain how to use the project. Include any configuration steps, command-line options, or other relevant information.

Example:

### For Task 1 

```bash
python task1.py
```

### For Task 2

1. Run `main.py`.

   ```bash
   python main.py
   ```

2. Import Postman Collection in Postman for FastAPI implementation. Open Postman

   **File > Import > select or drop file `Postman Collection/Finzome Task Collection.postman_collection.json`.**

3. Send Post request(Make sure `main.py` is running & the request body is selected with form-data with the file of data)

   <img width="100%" alt="Screenshot 2024-01-22 at 1 40 14 PM" src="https://github.com/parthdasawant/finzome_tasks/assets/80618762/cae21992-cd91-4192-ae92-09e6c85164d6">
