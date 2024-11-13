"""initial migration

Revision ID: d25f48d22909
Revises: 
Create Date: 2024-11-13 17:08:34.467306

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d25f48d22909"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "urls",
        sa.Column("long_url", sa.String(), nullable=False),
        sa.Column("short_url", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("long_url", "short_url"),
    )
    op.create_index(
        op.f("ix_urls_long_url"), "urls", ["long_url"], unique=True
    )
    op.create_index(
        op.f("ix_urls_short_url"), "urls", ["short_url"], unique=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_urls_short_url"), table_name="urls")
    op.drop_index(op.f("ix_urls_long_url"), table_name="urls")
    op.drop_table("urls")
    # ### end Alembic commands ###