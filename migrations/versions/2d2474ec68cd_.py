"""empty message

Revision ID: 2d2474ec68cd
Revises: 175ebdddddd2
Create Date: 2023-02-16 17:59:36.621884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d2474ec68cd'
down_revision = '175ebdddddd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('operation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted', sa.Boolean(), server_default='false', nullable=False, default=False))

    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted', sa.Boolean(), server_default='false', nullable=False, default=False))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted', sa.Boolean(), server_default='false', nullable=False, default=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('deleted')

    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.drop_column('deleted')

    with op.batch_alter_table('operation', schema=None) as batch_op:
        batch_op.drop_column('deleted')

    # ### end Alembic commands ###