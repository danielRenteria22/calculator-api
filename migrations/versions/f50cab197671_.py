"""empty message

Revision ID: f50cab197671
Revises: 32d4919c2e8a
Create Date: 2023-02-16 10:49:42.005775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f50cab197671'
down_revision = '32d4919c2e8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column('operation_response',
               existing_type=sa.INTEGER(),
               type_=sa.Double(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column('operation_response',
               existing_type=sa.Double(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
