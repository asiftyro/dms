"""empty message

Revision ID: 1037adf175a9
Revises: 
Create Date: 2021-09-11 18:02:47.864893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1037adf175a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('merchant_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todo', sa.String(length=128), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    op.drop_table('orders')
    # ### end Alembic commands ###
