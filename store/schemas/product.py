from pydantic import Field
from store.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: str = Field(description="Product name")
    quantity: int = Field(description="Product quantity")
    price: int = Field(description="Product price")
    status: str = Field(description="Product status")
