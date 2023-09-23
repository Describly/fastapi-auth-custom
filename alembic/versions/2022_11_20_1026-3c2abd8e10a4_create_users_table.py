"""create users table

Revision ID: 3c2abd8e10a4
Revises: 
Create Date: 2022-11-20 10:26:56.410665

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision = '3c2abd8e10a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('first_name', sa.String(100), nullable=True),
        sa.Column('last_name', sa.String(100), nullable=True),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('password', sa.String(100), nullable=False),
        sa.Column('is_active', sa.Boolean, default=False),
        sa.Column('is_verified', sa.Boolean, default=False),
        sa.Column('verified_at', sa.DateTime, nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=True, onupdate=datetime.now),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
