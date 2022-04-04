"""add Evaluation model

Revision ID: 647c510a77b1
Revises: 806f5dcb11bf
Create Date: 2020-05-07 16:33:36.216423

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "647c510a77b1"
down_revision = "806f5dcb11bf"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "evaluation",
        sa.Column("eval_hash", sa.String(length=40), nullable=False),
        sa.Column("task_hash", sa.String(length=40), nullable=False),
        sa.Column("args_hash", sa.String(length=40), nullable=False),
        sa.Column("value_hash", sa.String(length=40), nullable=False),
        sa.ForeignKeyConstraint(
            ["task_hash"],
            ["task.hash"],
        ),
        sa.ForeignKeyConstraint(
            ["value_hash"],
            ["value.value_hash"],
        ),
        sa.PrimaryKeyConstraint("eval_hash"),
    )
    op.create_index(op.f("ix_evaluation_task_hash"), "evaluation", ["task_hash"], unique=False)
    op.create_index(op.f("ix_evaluation_value_hash"), "evaluation", ["value_hash"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_evaluation_value_hash"), table_name="evaluation")
    op.drop_index(op.f("ix_evaluation_task_hash"), table_name="evaluation")
    op.drop_table("evaluation")
    # ### end Alembic commands ###
