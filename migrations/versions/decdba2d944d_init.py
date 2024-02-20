"""Init

Revision ID: decdba2d944d
Revises: 
Create Date: 2024-02-20 11:26:54.022149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'decdba2d944d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('creators', sa.ARRAY(sa.Integer()), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('presentations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('conference', sa.String(), nullable=False),
    sa.Column('publicationDate', sa.String(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=False),
    sa.Column('place', sa.String(), nullable=True),
    sa.Column('kind', sa.Enum('ORAL', 'POSTER', 'INVITED', 'PLENAR', name='kind', native_enum=False), nullable=False),
    sa.Column('presentationid', sa.String(), nullable=False),
    sa.Column('confid', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('creators', sa.ARRAY(sa.Integer()), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('presentationid')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('irid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('irid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('presentations')
    op.drop_table('patents')
    # ### end Alembic commands ###