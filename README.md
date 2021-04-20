- This is a project referenced from [adilmoujahid/blockchain-python-tutorial](https://github.com/adilmoujahid/blockchain-python-tutorial), and [miguelgrinberg/microblog](https://github.com/adilmoujahid/blockchain-python-tutorial).
- apllicable to Python>=3.6
# Features
- Flask based blockchain exchange API
- sqlalchemy orm database for user and transactions.

# Usage
1. Create a virtual enviroment in your targeted dirtionary.
2. Install all the required packages by `pip install -r requirements.txt`
3. Create the migration repository by `flask db init`
4. migrate the database by `flask db migrate`
5. Generates the migration script by `flask db upgrade`
6. setting the environment variable by `export FLASK_APP=microblog.py` (linux) or `SET FLASK_APP=microblog.py` (windows)
7. Set enviroment variable by creating a .flaskenv file (`pip install python-dotenv` required) and set `FLASK_APP=microblog.py` in .flaskenv file. 
8. run `flask run` to start the server. The server node is set `127.0.0.1:5000` by default.
