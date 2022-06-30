"""Add Usuario e Relacionamentos_3

Revision ID: 3cd632970278
Revises: d79e46c97729
Create Date: 2022-06-19 20:41:51.200028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cd632970278'
down_revision = 'd79e46c97729'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('telefone', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Usuario', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Usuario_id'), ['id'], unique=False)

    with op.batch_alter_table('Produto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_usuario', 'Usuario', ['usuario_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Produto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_usuario', type_='foreignkey')
        batch_op.drop_column('usuario_id')

    with op.batch_alter_table('Usuario', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Usuario_id'))

    op.drop_table('Usuario')
    # ### end Alembic commands ###
