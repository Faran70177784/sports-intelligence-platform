"""
Generic repository.

Provides reusable CRUD operations for SQLAlchemy models.
"""

from typing import Generic
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Generic repository.
    """

    def __init__(
        self,
        db: Session,
        model: Type[ModelType],
    ):

        self.db = db
        self.model = model

    def get_all(self) -> List[ModelType]:

        return self.db.query(self.model).all()

    def get_by_id(self, object_id: int) -> Optional[ModelType]:

        return (
            self.db.query(self.model)
            .filter(self.model.id == object_id)
            .first()
        )

    def create(self, obj: ModelType):

        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj

    def delete(self, obj: ModelType):

        self.db.delete(obj)
        self.db.commit()