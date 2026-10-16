"""add product constraints

Revision ID: 3853aa5530bd
Revises: fcc078c1f44f
Create Date: 2026-10-15 22:13:32.665143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3853aa5530bd'
down_revision: Union[str, Sequence[str], None] = 'fcc078c1f44f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint("ck_product_price_non_negative", "products",type_="check")
    op.create_check_constraint("ck_product_price_non_negative", "products","price > 0")


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("ck_product_price_non_negative", "products",type_="check")
    op.create_check_constraint("ck_product_price_non_negative","products","price >= 0")