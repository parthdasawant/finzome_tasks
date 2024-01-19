## General Guidelines:
1. Follow standard Python code style practices (PEP-8).
2. Assignment should be a .py file.
3. If external packages are required, then don’t forget to add requirements.txt file.
4. Use meaningful variable names. Code should be properly structured and readable.
5. Try to write an optimized with minimum complexity.
### Task1:
Calculate the Daily Volatility and annualized volatility for the dataset in Python. Please use the data file from here.
You can download similar files from nseindia website. Implement the formulas:
1. Daily Returns = (current close / previous close) - 1 (This will be a data series)
2. Daily Volatility = Standard Deviation (Daily Returns) (This will be a single value)
3. Annualized Volatility = Daily Volatility * Square Root (length of data) (This will be a single value)
You can decide on whatever tools/packages you need to implement the above data calculations.
### Task2:
Make a http endpoint using any one of the python web frameworks – FastAPI or Flask or Django. Implement following Functionality:
1. Accept a csv file or a parameter with which data can be fetched from directory. (like file used in Task1)
2. Compute Daily, Annualized volatility and return these values.
You can decide on the endpoint name, file headers and other required parameters for the functionality implementation.
Please mention in the docstrings what parameters name and headers were chosen.
