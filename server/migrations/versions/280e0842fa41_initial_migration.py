"""Initial migration.

Revision ID: 280e0842fa41
Revises: 
Create Date: 2025-06-10 11:40:10.615079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '280e0842fa41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'departments')
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')

    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    op.drop_table('employees')
    op.drop_table('departments')
    # ### end Alembic commands ###
