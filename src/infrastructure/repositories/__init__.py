# infrastructure/repositories/__init__.py

from .repository import Repository
from .product_repository import ProductRepository
from .category_repository import CategoryRepository

__all__ = ['Repository', 'ProductRepository', 'CategoryRepository']
