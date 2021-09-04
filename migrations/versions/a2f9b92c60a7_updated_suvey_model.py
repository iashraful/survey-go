"""updated suvey model

Revision ID: a2f9b92c60a7
Revises: a80f06bb2582
Create Date: 2021-09-04 19:17:41.789790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f9b92c60a7'
down_revision = 'a80f06bb2582'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('survey_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'questions', 'surveys', ['survey_id'], ['id'])
    op.add_column('surveys', sa.Column('published_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('surveys', 'published_time')
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.drop_column('questions', 'survey_id')
    # ### end Alembic commands ###