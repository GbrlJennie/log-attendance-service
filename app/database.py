from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pytz

# Setup SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./attendance.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class AttendanceLog(Base):
    __tablename__ = "attendance_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    event_type = Column(String)  # CHECK_IN / CHECK_OUT
    category = Column(String)    # WFO, WFH, SAKIT, IZIN
    notes = Column(Text, nullable=True) # Keterangan tambahan (misal: "Sakit Demam")
    timestamp = Column(DateTime, default=lambda: datetime.now(pytz.timezone('Asia/Jakarta')))
    
    # Tambahan: Node ID (Simulasi identitas STB)
    node_id = Column(String, default="STB-001") 

def init_db():
    Base.metadata.create_all(bind=engine)