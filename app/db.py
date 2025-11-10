from collections.abc import AsyncGenerator
import uuid

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID