"""removed-tasks-model

Revision ID: 65a5e01ceadb
Revises: 52e27cb7d257
Create Date: 2021-09-07 05:37:59.782386

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '65a5e01ceadb'
down_revision = '52e27cb7d257'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tasks_id', table_name='tasks')
    op.drop_table('tasks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('execution_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tasks_pkey')
    )
    op.create_index('ix_tasks_id', 'tasks', ['id'], unique=False)
    # ### end Alembic commands ###
