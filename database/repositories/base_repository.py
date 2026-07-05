"""
Base repository providing common CRUD operations.
"""

from typing import Generic, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Generic repository for CRUD operations.
    """

    def __init__(
        self,
        db: Session,
        model: type[ModelType],
    ) -> None:
        self.db = db
        self.model = model

    def create(
        self,
        entity: ModelType,
    ) -> ModelType:

        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def get_all(self) -> list[ModelType]:

        return self.db.query(self.model).all()

    def get_by_id(
        self,
        entity_id: int,
    ) -> ModelType | None:

        return (
            self.db.query(self.model)
            .filter(self.model.id == entity_id)
            .first()
        )

    def update(self) -> None:

        self.db.commit()

    def delete(
        self,
        entity: ModelType,
    ) -> None:

        self.db.delete(entity)
        self.db.commit()