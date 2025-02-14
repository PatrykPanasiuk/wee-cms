from backend.database import Base, engine

def init_db():
    """Tworzy bazę danych i tabele, jeśli jeszcze nie istnieją."""
    print("📌 Tworzenie bazy danych...")
    Base.metadata.create_all(bind=engine)
    print("✅ Baza danych gotowa!")

if __name__ == "__main__":
    init_db()