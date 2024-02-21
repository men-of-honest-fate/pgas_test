"""Grants

Revision ID: e8e1aa532aa3
Revises: 7947c0101452
Create Date: 2024-02-21 15:45:20.042413

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'e8e1aa532aa3'
down_revision = '7947c0101452'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('dates_begin', sa.DateTime(), nullable=False),
    sa.Column('dates_end', sa.DateTime(), nullable=False),
    sa.Column('department', sa.String(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('creators', sa.ARRAY(sa.Integer()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grant')
    # ### end Alembic commands ###