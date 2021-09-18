"""empty message

Revision ID: 0c9818550c2d
Revises: e2f1f2d6e1db
Create Date: 2021-09-19 01:01:37.934242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c9818550c2d'
down_revision = 'e2f1f2d6e1db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email_confirmed_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email_confirmed_at')
    # ### end Alembic commands ###
