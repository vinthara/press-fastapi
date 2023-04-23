"""Add press details data

Revision ID: 93e3cb2b3fcf
Revises: ea6b75090bef
Create Date: 2023-04-23 16:36:14.654127

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData
from sqlalchemy.sql import table

# revision identifiers, used by Alembic.
revision = "93e3cb2b3fcf"
down_revision = "ea6b75090bef"
branch_labels = None
depends_on = None


def upgrade() -> None:
    rows = [
        {
            "id": "LKR",
            "name": "LEKRISHNA",
            "address": "73, rue Doudeauville",
            "city": "Paris",
            "zip_code": 75018,
        },
        {
            "id": "RP",
            "name": "RUPI",
            "address": "73, rue Labat",
            "city": "Paris",
            "zip_code": 75018,
        },
        {
            "id": "SKT",
            "name": "SANKEET",
            "address": "39, boulevard de la Chapelle",
            "city": "Paris",
            "zip_code": 75010,
        },
        {
            "id": "LKT",
            "name": "LANKEET",
            "address": "39 boulevard de la Chapelle",
            "city": "Paris",
            "zip_code": 75010,
        },
    ]
    my_table = sa.Table("PRESS", sa.MetaData(), autoload_with=op.get_bind())
    op.bulk_insert(my_table, rows)


def downgrade() -> None:
    op.execute("DELETE FROM PRESS;")
