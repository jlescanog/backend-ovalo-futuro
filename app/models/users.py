from sqlalchemy import Column, Integer, String, Date, Boolean, Text, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
from app.schemas.roles import roles_usuario  # Asumiendo que roles_usuario es un Enum definido en otro lugar

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(150), nullable=False)
    apellidos = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False, check_constraint="fecha_nacimiento < CURRENT_DATE")
    tipo_documento = Column(String(20), nullable=False)
    numero_doc = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(15))
    password_hash = Column(Text, nullable=False)
    rol = Column(Enum(roles_usuario), nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    fecha_creacion = Column(TIMESTAMP, default=func.now(), nullable=False)
    fecha_actualizacion = Column(TIMESTAMP)
    quien_modifico = Column(Integer, ForeignKey('usuarios.id'))
    fecha_modificacion = Column(TIMESTAMP)
    ip_modificacion = Column(String(50))