from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Motor asíncrono para PostgreSQL
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True  # Muestra queries en consola (solo para desarrollo)
)

# Sesión asíncrona
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session