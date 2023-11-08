from msilib import Table
from sqlalchemy import ForeignKey, MetaData, create_engine, table, Column, String, Integer

metadata_db_obj = MetaData(schema="bank")
financial_info = Table(
    "financial_info",
    metadata_db_obj,
    Column("id", Integer, primary_key=True),
    Column("value", String(100), nullable=False)
)

print(financial_info.primary_key)