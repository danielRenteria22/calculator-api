"""empty message

Revision ID: 3b92bad68445
Revises: b539af9ec631
Create Date: 2023-02-16 11:31:02.635166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b92bad68445'
down_revision = 'b539af9ec631'
branch_labels = None
depends_on = None


def upgrade():
    with op.get_context().autocommit_block():
        op.execute("ALTER TYPE operationtypes ADD VALUE 'ADD_CREDIT'")


def downgrade():
    op.execute("ALTER TYPE operationtypes RENAME TO operationtypes_old")
    op.execute("CREATE TYPE operationtypes AS ENUM('ADDITION', 'SUBSTRACTION', 'MULTIPLICATION', 'DIVISION', 'SQUARE_ROOT', 'RANDOM_STRING')")
    op.execute((
        "ALTER TABLE operation ALTER COLUMN type TYPE operationtypes USING "
        "status::text::operationtypes"
    ))
    op.execute("DROP TYPE operationtypes_old")
