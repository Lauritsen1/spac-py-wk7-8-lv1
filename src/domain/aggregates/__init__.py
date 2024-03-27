# domain/aggregates/__init__.py

from .transaction import Transaction
from .transaction import TransactionType

__all__ = ['Transaction', 'TransactionType']
