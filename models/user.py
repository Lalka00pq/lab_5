import psycopg2
from config import DATABASE_URL

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: Optional[datetime] = None
