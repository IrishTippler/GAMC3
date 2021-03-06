"""empty message

Revision ID: 85c4a7496722
Revises: ecbdd124fffb
Create Date: 2018-11-15 17:39:53.983835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85c4a7496722'
down_revision = 'ecbdd124fffb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('breed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('thcvalue', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('breed', sa.Integer(), nullable=True),
    sa.Column('datestart', sa.Date(), nullable=True),
    sa.Column('dateend', sa.Date(), nullable=True),
    sa.Column('growlength', sa.Integer(), nullable=True),
    sa.Column('soiltype', sa.Integer(), nullable=True),
    sa.Column('actual', sa.Binary(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grow')
    op.drop_table('breed')
    # ### end Alembic commands ###
