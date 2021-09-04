"""Initial Migration

Revision ID: 51c3a55cc6f8
Revises:
Create Date: 2021-09-04 14:26:51.867496

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '51c3a55cc6f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('tasks',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('execution_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='tasks_pkey')
                    )
    op.create_index('ix_tasks_id', 'tasks', ['id'], unique=False)


def downgrade():
    op.drop_index('ix_tasks_id', table_name='tasks')
    op.drop_table('tasks')
