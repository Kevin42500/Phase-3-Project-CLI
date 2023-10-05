from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_storage import User, Transaction  

# Database URL
DATABASE_URL = 'sqlite:///financial_data.db'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    
    session = Session()

    desired_username = 'Emily Johnson'

    user = session.query(User).filter_by(username=desired_username).first()

    if user:
     
        transactions = session.query(Transaction).filter_by(user_id=user.id).all()
        for transaction in transactions:
            session.delete(transaction)

        session.delete(user)

        session.commit()

        print(f"User '{desired_username}' and their transactions have been deleted.")
    else:
        print(f"User '{desired_username}' not found.")

   
    session.close()
