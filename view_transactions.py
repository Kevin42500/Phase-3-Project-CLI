from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_storage import User, Transaction  

DATABASE_URL = 'sqlite:///financial_data.db'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    session = Session()

    transactions = session.query(Transaction).all()

    for transaction in transactions:
        print(f"User: {transaction.user.username}")
        print(f"Transaction: {transaction.date}, {transaction.category.name}, {transaction.amount}")
        print()

    session.close()
