"""empty message

Revision ID: ecbdd124fffb
Revises: aede4d0e4aaa
Create Date: 2018-11-14 15:23:24.442846

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ecbdd124fffb'
down_revision = 'aede4d0e4aaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employees_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_employees_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_employees_last_name'), 'users', ['last_name'], unique=False)
    op.create_index(op.f('ix_employees_username'), 'users', ['username'], unique=True)
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name='user_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    op.drop_index(op.f('ix_employees_username'), table_name='users')
    op.drop_index(op.f('ix_employees_last_name'), table_name='users')
    op.drop_index(op.f('ix_employees_first_name'), table_name='users')
    op.drop_index(op.f('ix_employees_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
