"""added-section

Revision ID: f9b968761519
Revises: ca14b08b54e2
Create Date: 2021-09-16 06:57:47.798103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9b968761519'
down_revision = 'ca14b08b54e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sections_id'), 'sections', ['id'], unique=False)
    op.add_column('questions', sa.Column('section_id', sa.Integer(), nullable=True))
    op.add_column('questions', sa.Column('is_required', sa.Boolean(), nullable=True))
    op.create_foreign_key(None, 'questions', 'sections', ['section_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.drop_column('questions', 'is_required')
    op.drop_column('questions', 'section_id')
    op.drop_index(op.f('ix_sections_id'), table_name='sections')
    op.drop_table('sections')
    # ### end Alembic commands ###
