# my-first-repo

Learning and practicing version control!

More content

Adding this content uding the VS Code text editor (locally).

## Setup 
Clone the repo and download it from GitHub. Perhaps onto the desktop

Navigate to the repo using the command line.

```sh
cd ~/Desktop/my-first-repo
```
#Create a virtual environment:

```sh
conda create -n my-first-env-fall-2025 python=3.11
```

Activate the virtual environment:

```sh
conda activate my-first-env-fall-2025
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration
The stocks functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:


```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"
```
## Usage


```sh
python app/my_script.py
```

#Game of rock, paper, scissors:

```sh
python app/rps.py


Run tests:

```sh
pytest
```
### Web App
Run the web app
```sh

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run

## Testing
