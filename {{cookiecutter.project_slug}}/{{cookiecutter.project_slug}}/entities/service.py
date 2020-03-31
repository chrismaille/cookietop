from sqlalchemy import Column, Integer, String, DateTime

from initializers.sql import Base


class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    created = Column(DateTime)

    def __str__(self):
        return f"<Service(id={self.id}, name={self.name}>, description={self.description})>"
