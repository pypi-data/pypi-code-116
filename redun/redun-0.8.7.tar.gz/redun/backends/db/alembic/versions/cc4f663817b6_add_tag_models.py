"""Add Tag models

Revision ID: cc4f663817b6
Revises: 647c510a77b1
Create Date: 2020-08-16 19:39:28.772684

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "cc4f663817b6"
down_revision = "cd2d53191748"
branch_labels = None
depends_on = None


def upgrade():
    if op.get_bind().dialect.name == "postgresql":
        json_type = sa.dialects.postgresql.JSONB
    else:
        json_type = sa.String

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tag",
        sa.Column("tag_hash", sa.String(length=40), nullable=False),
        sa.Column(
            "entity_type",
            sa.Enum("Execution", "Job", "CallNode", "Task", "Value", "Null", name="tagentitytype"),
            nullable=False,
        ),
        sa.Column("entity_id", sa.String(), nullable=False),
        sa.Column("key", sa.String(), nullable=False),
        sa.Column("value", json_type, nullable=False),
        sa.Column("is_current", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("tag_hash"),
    )
    op.create_index(op.f("ix_tag_entity_id"), "tag", ["entity_id"], unique=False)
    op.create_index(op.f("ix_tag_key"), "tag", ["key"], unique=False)
    op.create_index(op.f("ix_tag_value"), "tag", ["value"], unique=False)
    op.create_index(
        "ix_tag_tag_hash_current",
        "tag",
        ["tag_hash"],
        unique=True,
        postgresql_where=sa.text("is_current"),
        sqlite_where=sa.text("is_current"),
    )

    op.create_table(
        "tag_edit",
        sa.Column("parent_id", sa.String(), nullable=False),
        sa.Column("child_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["child_id"],
            ["tag.tag_hash"],
        ),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["tag.tag_hash"],
        ),
        sa.PrimaryKeyConstraint("parent_id", "child_id"),
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tag_edit")
    op.drop_table("tag")
    # ### end Alembic commands ###
