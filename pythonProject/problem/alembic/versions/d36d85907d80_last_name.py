"""last_name

Revision ID: d36d85907d80
Revises: 7d8fb40abbaa
Create Date: 2022-06-20 11:47:15.263031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd36d85907d80'
down_revision = '7d8fb40abbaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_name')
    # ### end Alembic commands ###