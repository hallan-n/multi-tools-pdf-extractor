from sqlalchemy.orm import declarative_base

BaseModel = declarative_base()
class Base(BaseModel):
    __abstract__ = True