import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models import Store, Table, TableSession, Menu, Category
from app.auth import get_password_hash
import uuid

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture
def test_data(db):
    store = Store(
        id=str(uuid.uuid4()),
        name="Test Store",
        code="TEST001"
    )
    db.add(store)
    
    table = Table(
        id=str(uuid.uuid4()),
        store_id=store.id,
        table_number=1,
        password_hash=get_password_hash("1234")
    )
    db.add(table)
    
    session = TableSession(
        id=str(uuid.uuid4()),
        table_id=table.id
    )
    db.add(session)
    
    category = Category(
        id=str(uuid.uuid4()),
        store_id=store.id,
        name="Test Category",
        display_order=1
    )
    db.add(category)
    
    menu1 = Menu(
        id="menu-1",
        category_id=category.id,
        name="Test Menu 1",
        price=10000,
        is_available=True
    )
    menu2 = Menu(
        id="menu-2",
        category_id=category.id,
        name="Test Menu 2",
        price=20000,
        is_available=True
    )
    db.add_all([menu1, menu2])
    db.commit()
    
    return {
        "store": store,
        "table": table,
        "session": session,
        "menu1": menu1,
        "menu2": menu2
    }
