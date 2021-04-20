from app import app, db
from app.models import User,Transactions
from backend import blockchain1,wallet

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User,'Transactions':Transactions}
