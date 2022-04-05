from __future__ import annotations

import pytest

from metricflow.sql.render.sql_plan_renderer import SqlQueryPlanRenderer, DefaultSqlQueryPlanRenderer


@pytest.fixture
def default_sql_plan_renderer() -> SqlQueryPlanRenderer:  # noqa: D
    return DefaultSqlQueryPlanRenderer()
