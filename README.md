# API Testing with Pytest, Python, and Requests
**Overview**
This repository contains automated API tests implemented using Pytest, Python, and the Requests library. 
The tests are designed to validate the functionality of an API endpoint by sending HTTP requests and verifying the responses.
This was inspired in the challenges presented here https://apichallenges.eviltester.com/gui/challenges, by Alan Richardson

**Features**
- Comprehensive test suite covering various scenarios.
- Utilizes Page Object Model (POM) for better organization and maintainability.
- Provides examples of common API testing patterns and best practices.
- Easy setup and execution using Pytest.

**Requirements**
* Python 3.x
* Pytest
* Requests

**Installation**
- Clone the repository to your local machine:
`git clone git@github.com:karlamieses/api-automation-pytest-python.git `

- Navigate to the project directory
- Install the required dependencies:
`pip install -r requirements.txt`
or
`pip3 install -r requirements.txt`

**Usage**
To run the tests subsequently, execute the following command in the terminal:
`pytest`
To run the tests in parallel and generate an HTML report
`pytest -n auto --html=report.html`  

**Test Structure**
The tests are organized into directories and follow the Page Object Model (POM) design pattern for improved 
maintainability and readability.

tests/: Contains test scripts organized by functionality.
fixtures/: Contains reusable queries.
resources/: Contains utility functions, request headers, and URLs.

**Test Cases**
Validating GET Requests
Validating POST Requests
Validating PUT Requests

**Contributing**
Contributions are welcome! If you have suggestions, feature requests, or bug reports, please open an issue or submit a pull request.