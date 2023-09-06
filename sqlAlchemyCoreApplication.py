from msilib import Table
from sqlalchemy import ForeignKey, MetaData, create_engine, table, Column, String, Integer

engine = create_engine("sqlite://")

# Objeto que será um metadado associado ao metadados do db
metadata_obj = MetaData(schema="teste")

# Criando as tabelas
# user = Table(
#     "user",
#     metadata_obj,
#     Column("user_id", Integer, primary_key=True),
#     Column("user_name", String(16), nullable=False),
#     Column("email_address", String(60)),
#     Column("nickname", String(50), nullable=False),
# )

# user_perfs = Table(
#     "user_perfs", metadata_obj,
#     Column("pref_id", Integer, primary_key=True),
#     Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
#     Column("pref_name", String(60)),
#     Column("pref_value", String(50), nullable=False)
# )

# for tables in metadata_obj.sorted_tables:
#     print(tables)

metadata_db_obj = MetaData(schema="bank")
financial_info = Table(
    "financial_info",
    metadata_db_obj,
    Column("id", Integer, primary_key=True),
    Column("value", String(100), nullable=False)
)

print(financial_info.primary_key)