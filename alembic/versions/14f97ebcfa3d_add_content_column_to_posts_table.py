"""add content column to posts table

Revision ID: 14f97ebcfa3d
Revises: 4529146cccf5
Create Date: 2021-12-20 16:16:40.341161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14f97ebcfa3d'
down_revision = '4529146cccf5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
