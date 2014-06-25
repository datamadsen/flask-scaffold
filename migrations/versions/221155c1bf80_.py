"""empty message

Revision ID: 221155c1bf80
Revises: None
Create Date: 2013-08-06 14:59:01.930216

"""

# revision identifiers, used by Alembic.
revision = '221155c1bf80'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('foo', sa.Column('created', sa.DateTime(timezone=True), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('foo', 'created')
    ### end Alembic commands ###