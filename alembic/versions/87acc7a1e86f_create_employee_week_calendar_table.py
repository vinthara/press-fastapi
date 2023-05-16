"""create EMPLOYEE_WEEK_CALENDAR table

Revision ID: 87acc7a1e86f
Revises: 93e3cb2b3fcf
Create Date: 2023-05-01 14:47:23.749344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "87acc7a1e86f"
down_revision = "93e3cb2b3fcf"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "EMPLOYEE_WEEK_CALENDAR",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("employee_id", sa.Integer(), nullable=False),
        sa.Column("press_id", sa.String(), nullable=False),
        sa.Column("week_day", sa.Integer(), nullable=False),
        sa.Column("shift_number", sa.Integer(), nullable=False),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("end_time", sa.Time(), nullable=False),
        sa.ForeignKeyConstraint(
            ["employee_id"],
            ["EMPLOYEE.id"],
        ),
        sa.ForeignKeyConstraint(
            ["press_id"],
            ["PRESS.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("employee_id", "press_id", "week_day", "shift_number"),
        sa.CheckConstraint("start_time < end_time"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("EMPLOYEE_WEEK_CALENDAR")
    # ### end Alembic commands ###