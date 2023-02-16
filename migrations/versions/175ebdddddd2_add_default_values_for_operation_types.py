"""Add default values for operation types

Revision ID: 175ebdddddd2
Revises: 3b92bad68445
Create Date: 2023-02-16 11:43:26.845603

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

from models.operation import OperationTypes

# revision identifiers, used by Alembic.
revision = '175ebdddddd2'
down_revision = '3b92bad68445'
branch_labels = None
depends_on = None


def upgrade():
    operation_table = table('operation',
        column('id', Integer),
        column('cost', Integer),
        column('type', String)
    )

    operations = [
        {
            'cost': 5,
            'type': OperationTypes.ADDITION.value
        },
        {
            'cost': 5,
            'type': OperationTypes.SUBSTRACTION.value
        },
        {
            'cost': 10,
            'type': OperationTypes.MULTIPLICATION.value
        },
        {
            'cost': 10,
            'type': OperationTypes.DIVISION.value
        },
        {
            'cost': 15,
            'type': OperationTypes.SQUARE_ROOT.value
        },
        {
            'cost': 20,
            'type': OperationTypes.RANDOM_STRING.value
        },
        {
            'cost': 0,
            'type': OperationTypes.ADD_CREDIT.value
        },
    ]
    op.bulk_insert(operation_table,operations)


def downgrade():
    op.execute("DELETE FROM operation where id > 0")
