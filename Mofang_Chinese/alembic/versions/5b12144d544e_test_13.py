"""test 13

Revision ID: 5b12144d544e
Revises: 93ddf329b58e
Create Date: 2022-07-19 12:40:18.020009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b12144d544e'
down_revision = '93ddf329b58e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('WordsToUsers', sa.Column('words', sa.Integer(), nullable=True))
    op.add_column('WordsToUsers', sa.Column('users', sa.Integer(), nullable=True))
    op.add_column('WordsToUsers', sa.Column('learn_state', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'WordsToUsers', 'users', ['users'], ['id'])
    op.create_foreign_key(None, 'WordsToUsers', 'words', ['words'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'WordsToUsers', type_='foreignkey')
    op.drop_constraint(None, 'WordsToUsers', type_='foreignkey')
    op.drop_column('WordsToUsers', 'learn_state')
    op.drop_column('WordsToUsers', 'users')
    op.drop_column('WordsToUsers', 'words')
    # ### end Alembic commands ###