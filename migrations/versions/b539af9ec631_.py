"""empty message

Revision ID: b539af9ec631
Revises: f50cab197671
Create Date: 2023-02-16 10:51:58.240276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b539af9ec631'
down_revision = 'f50cab197671'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column('operation_response',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column('operation_response',
               existing_type=sa.String(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)

    # ### end Alembic commands ###