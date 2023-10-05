from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

DATABASE_URL = 'sqlite:///financial_data.db'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    transactions = relationship('Transaction', back_populates='user')

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    description = Column(String)
    amount = Column(Float, nullable=False)
    user = relationship('User', back_populates='transactions')
    category = relationship('Category', back_populates='transactions')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    transactions = relationship('Transaction', back_populates='category')

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    session = Session()

    entertainment_category = Category(name="Entertainment")
    travel_category = Category(name="Travel")
    healthcare_category = Category(name="Healthcare")
    education_category = Category(name="Education")
    session.add_all([entertainment_category, travel_category, healthcare_category, education_category])

    user1 = User(username="Gray Developer", password="contract")
    user2 = User(username="Manchester Black", password="supergirl")
    user3 = User(username="Kinuthia Mutai", password="hustler")
    user4 = User(username="Humphrey Kibet", password="snowball")
    session.add_all([user1, user2, user3, user4])

    more_transactions_data = [
        {"user": user1, "date": "2023-10-07", "category": entertainment_category, "description": "Movie night", "amount": 50.0},
        {"user": user2, "date": "2023-10-08", "category": travel_category, "description": "Flight ticket", "amount": 350.0},
        {"user": user3, "date": "2023-10-07", "category": healthcare_category, "description": "Doctor's appointment", "amount": 90.0},
        {"user": user4, "date": "2023-10-08", "category": education_category, "description": "Tutors", "amount": 120.0},
    ]
    more_transactions = [Transaction(**data) for data in more_transactions_data]
    session.add_all(more_transactions)
    session.commit()

    users = session.query(User).all()
    for user in users:
        print(f"User: {user.username}")
        for transaction in user.transactions:
            print(f"Transaction: {transaction.date}, {transaction.category.name}, {transaction.amount}")

    session.close()
