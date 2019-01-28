"""empty message

Revision ID: 6069134b485f
Revises: 83f37c9bd2bf
Create Date: 2019-01-27 20:28:23.160198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6069134b485f'
down_revision = '83f37c9bd2bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('translate',
    sa.Column('fir_word_id', sa.Integer(), nullable=True),
    sa.Column('sec_word_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fir_word_id'], ['word.id'], ),
    sa.ForeignKeyConstraint(['sec_word_id'], ['word.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translate')
    # ### end Alembic commands ###
