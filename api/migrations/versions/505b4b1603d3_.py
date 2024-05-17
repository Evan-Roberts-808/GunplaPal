"""empty message

Revision ID: 505b4b1603d3
Revises: 
Create Date: 2024-05-16 20:04:59.179777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '505b4b1603d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gunplas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_img', sa.String(), nullable=True),
    sa.Column('grade', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('model_num', sa.String(), nullable=True),
    sa.Column('series', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('release_date', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_gunplas'))
    )
    op.create_table('themes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_themes'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('theme_id', sa.Integer(), nullable=True),
    sa.Column('profile_pic', sa.String(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('skill_level', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['theme_id'], ['themes.id'], name=op.f('fk_users_theme_id_themes')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    op.create_table('collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('custom_img', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('gunpla_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gunpla_id'], ['gunplas.id'], name=op.f('fk_collections_gunpla_id_gunplas')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_collections_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_collections'))
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('gunpla_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['gunpla_id'], ['gunplas.id'], name=op.f('fk_comments_gunpla_id_gunplas')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_comments_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_comments'))
    )
    op.create_table('wishlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('gunpla_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gunpla_id'], ['gunplas.id'], name=op.f('fk_wishlists_gunpla_id_gunplas')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_wishlists_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_wishlists'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishlists')
    op.drop_table('comments')
    op.drop_table('collections')
    op.drop_table('users')
    op.drop_table('themes')
    op.drop_table('gunplas')
    # ### end Alembic commands ###
