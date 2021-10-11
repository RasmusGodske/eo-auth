"""empty message

Revision ID: 7e4a75371b7f
Revises: 
Create Date: 2021-09-27 10:48:58.645356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e4a75371b7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_login_record_id'), 'login_record', ['id'], unique=False)
    op.create_index(op.f('ix_login_record_subject'), 'login_record', ['subject'], unique=False)
    op.create_table('token',
    sa.Column('opaque_token', sa.String(), nullable=False),
    sa.Column('internal_token', sa.String(), nullable=False),
    sa.Column('issued', sa.DateTime(timezone=True), nullable=False),
    sa.Column('expires', sa.DateTime(timezone=True), nullable=False),
    sa.Column('subject', sa.String(), nullable=False),
    sa.CheckConstraint('issued < expires'),
    sa.PrimaryKeyConstraint('opaque_token'),
    sa.UniqueConstraint('opaque_token')
    )
    op.create_index(op.f('ix_token_opaque_token'), 'token', ['opaque_token'], unique=False)
    op.create_index(op.f('ix_token_subject'), 'token', ['subject'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_token_subject'), table_name='token')
    op.drop_index(op.f('ix_token_opaque_token'), table_name='token')
    op.drop_table('token')
    op.drop_index(op.f('ix_login_record_subject'), table_name='login_record')
    op.drop_index(op.f('ix_login_record_id'), table_name='login_record')
    op.drop_table('login_record')
    # ### end Alembic commands ###