# Zerodha Report Extractor

This tool is used to extract tradebook snapshot from console.zerodha.com. You need to provide user details to this tool and it will extract snapshot for each segment and the month that you specify. You can use it to generate monthly transaction report.

##### How it works:

- This tool relies on firefox selenium driver to open the web page and perform report generation task.
- Once report is generated for a particular segment it is captured as a snapshot
- All such shapshots are bundled into a pdf to be used for submission purpose.

##### Built on:

Below are the libraries that will be used by this tool

- python
- selenium
- pillow

##### How to use:

1. Make sure you have python installed on your machine.
2. Download this project in your machine.
3. Install pipenv using `pip install pipenv`.
4. Run command `pipenv install` to download all dependencies.
5. Enter pipenv shell using `pipenv shell`.
6. Add required details in properties file.
7. Run `python app.py`.
