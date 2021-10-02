"""empty message

Revision ID: 23d7bd2f4023
Revises: 0c9818550c2d
Create Date: 2021-10-01 22:15:35.378753

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '23d7bd2f4023'
down_revision = '0c9818550c2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('merchants', sa.Column('trade_license', sa.String(length=256), nullable=True))
    op.add_column('merchants', sa.Column('tnc', mysql.BIGINT(unsigned=True), nullable=True))
    op.add_column('merchants', sa.Column('rate', mysql.BIGINT(unsigned=True), nullable=True))
    op.add_column('merchants', sa.Column('website', sa.String(length=256), nullable=True))
    op.add_column('merchants', sa.Column('facebook', sa.String(length=256), nullable=True))
    op.add_column('merchants', sa.Column('contact_name', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('contact_designation', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('contact_address', sa.String(length=256), nullable=True))
    op.add_column('merchants', sa.Column('contact_telephone', sa.String(length=32), nullable=True))
    op.add_column('merchants', sa.Column('contact_email', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('alt_contact_name', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('alt_contact_designation', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('alt_contact_address', sa.String(length=256), nullable=True))
    op.add_column('merchants', sa.Column('alt_contact_telephone', sa.String(length=32), nullable=True))
    op.add_column('merchants', sa.Column('alt_contact_email', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('collection_contact_name', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('collection_contact_designation', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('collection_contact_address', sa.String(length=256), nullable=True))
    op.add_column('merchants', sa.Column('collection_contact_telephone', sa.String(length=32), nullable=True))
    op.add_column('merchants', sa.Column('collection_contact_email', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('billing_contact_name', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('billing_contact_designation', sa.String(length=128), nullable=True))
    op.add_column('merchants', sa.Column('billing_contact_address', sa.String(length=256), nullable=True))
    op.add_column('merchants', sa.Column('billing_contact_telephone', sa.String(length=32), nullable=True))
    op.add_column('merchants', sa.Column('billing_contact_email', sa.String(length=128), nullable=True))
    op.drop_column('merchants', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('merchants', sa.Column('address', mysql.VARCHAR(length=256), nullable=True))
    op.drop_column('merchants', 'billing_contact_email')
    op.drop_column('merchants', 'billing_contact_telephone')
    op.drop_column('merchants', 'billing_contact_address')
    op.drop_column('merchants', 'billing_contact_designation')
    op.drop_column('merchants', 'billing_contact_name')
    op.drop_column('merchants', 'collection_contact_email')
    op.drop_column('merchants', 'collection_contact_telephone')
    op.drop_column('merchants', 'collection_contact_address')
    op.drop_column('merchants', 'collection_contact_designation')
    op.drop_column('merchants', 'collection_contact_name')
    op.drop_column('merchants', 'alt_contact_email')
    op.drop_column('merchants', 'alt_contact_telephone')
    op.drop_column('merchants', 'alt_contact_address')
    op.drop_column('merchants', 'alt_contact_designation')
    op.drop_column('merchants', 'alt_contact_name')
    op.drop_column('merchants', 'contact_email')
    op.drop_column('merchants', 'contact_telephone')
    op.drop_column('merchants', 'contact_address')
    op.drop_column('merchants', 'contact_designation')
    op.drop_column('merchants', 'contact_name')
    op.drop_column('merchants', 'facebook')
    op.drop_column('merchants', 'website')
    op.drop_column('merchants', 'rate')
    op.drop_column('merchants', 'tnc')
    op.drop_column('merchants', 'trade_license')
    # ### end Alembic commands ###
