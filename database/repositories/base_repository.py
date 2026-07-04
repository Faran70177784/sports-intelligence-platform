"""
Generic repository.

Reusable CRUD operations for SQLAlchemy models.
"""

from typing import Generic
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
    ) -> None:

        self.db = db
        self.model = model

    def get_all(self) -> list[ModelType]:

        return self.db.query(self.model).all()

    def get_by_id(
        self,
        object_id: int,
    ) -> Optional[ModelType]:

        return (
            self.db.query(self.model)
            .filter(self.model.id == object_id)
            .first()
        )

    def create(
        self,
        obj: ModelType,
    ) -> ModelType:

        self.db.add(obj)
        self.db.flush()
        self.db.refresh(obj)

        return obj

    def delete(
        self,
        obj: ModelType,
    ) -> None:

        self.db.delete(obj)
        self.db.flush()