# Coding Placement
## This repository is intended to be a resource for teams to gague a developer's ability. It should include a text document with instructions as well as the testing suite that will be testing against those instructions.
### Build this project with Python
Clone repo and `cd` into it  
- With Anaconda or Miniconda command line tool:  
`conda create -n placement python=3.10`  
`conda activate placement`  
`pip install --upgrade pip`  
`pip install virtualenv`  
`virtualenv -p python3.10 venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`

### Run Python tests with coverage/pytest
This command runs pytest via coverage:  
`coverage run -m pytest -vv`  
This command will print pytest report to stdout:  
`coverage report`  
This command will generate a coverage JSON file coverage.json in a directory called jsoncov:  
`coverage json -o jsoncov/coverage.json`  
This command will generate files including html files that highlight coverage in a directory called htmlcov:  
`coverage html`