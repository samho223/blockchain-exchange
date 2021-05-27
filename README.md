# Introduction
- This is a project referenced from [adilmoujahid/blockchain-python-tutorial](https://github.com/adilmoujahid/blockchain-python-tutorial), and [miguelgrinberg/microblog](https://github.com/adilmoujahid/blockchain-python-tutorial).
- appllicable to Python>=3.6
- This Web application is for demostrations only.
# Features
- a Flask based blockchain exchange 
- sqlalchemy ORM database for user and transactions.

# Usage
1. Create a virtual enviroment in your targeted dirtionary.
2. Install all the required packages by `pip install -r requirements.txt`
3. Create the migration repository by `flask db init`
4. migrate the database by `flask db migrate`
5. Generates the migration script by `flask db upgrade`
6. setting the environment variable by `export FLASK_APP=blockchain.py` (linux) or `SET FLASK_APP=blockchain.py` (windows)
7. (optional) Set enviroment variable by creating a .flaskenv file (`pip install python-dotenv` required) and set `FLASK_APP=blockchain.py` in .flaskenv file. 
8. run `flask run` to start the server. The server node is set `127.0.0.1:5000` by default.

# Application
- You must login first in order to access to index page.
- Every new user is forced yo register a new wallet for mining and transaction. Make sure you have noted down your private key !
- Create now blocks in index page, and create new transactions in Transaction page.
- You can visit other user's profile by `/user/<username>`, and make transactions to their public address.
- You can add new node for mining via configuration page.
- Have fun with this Blockchain Demo !
