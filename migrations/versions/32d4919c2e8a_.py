"""empty message

Revision ID: 32d4919c2e8a
Revises: 9e2ae7920ed2
Create Date: 2023-02-16 02:31:20.976354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32d4919c2e8a'
down_revision = '9e2ae7920ed2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.add_column(sa.Column('amount', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('user_balance', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('operation_response', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.drop_column('operation_response')
        batch_op.drop_column('user_balance')
        batch_op.drop_column('amount')

    # ### end Alembic commands ###
