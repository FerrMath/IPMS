"""Add validation that wasn't included automaticaly on the previous revision

Revision ID: fcc078c1f44f
Revises: 9e995f8d42be
Create Date: 2026-03-03 10:28:57.941787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcc078c1f44f'
down_revision: Union[str, Sequence[str], None] = '9e995f8d42be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_check_constraint(
        "ck_product_price_non_negative",
        "products",
        "price >= 0"
    )
    op.create_check_constraint(
        "ck_product_stock_non_negative",
        "products",
        "stock >= 0"
    )
    op.create_check_constraint(
        "ck_product_rating_range",
        "products",
        "rating >= 0 AND rating <= 5"
    )
    pass


def downgrade() -> None:
    op.drop_constraint("ck_product_price_non_negative", "products", type_="check")
    op.drop_constraint("ck_product_stock_non_negative", "products", type_="check")
    op.drop_constraint("ck_product_rating_range", "products", type_="check")
    pass
