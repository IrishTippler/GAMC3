"""empty message

Revision ID: aede4d0e4aaa
Revises: 
Create Date: 2018-11-14 11:39:27.278391

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'aede4d0e4aaa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_grow_name', table_name='grow')
    op.drop_table('grow')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grow',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('breed', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('growstart', sa.DATE(), nullable=True),
    sa.Column('growend', sa.DATE(), nullable=True),
    sa.Column('growlenght', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('soiltype', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('actual', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_grow_name', 'grow', ['name'], unique=False)
    # ### end Alembic commands ###
