from __future__ import annotations

import click
import datetime
import pandas as pd
import pytest

from click.testing import CliRunner, Result
from typing import List, Optional, Sequence

from metricflow.cli.cli_context import CLIContext
from metricflow.cli.models import Dimension, Materialization, Metric
from metricflow.engine.metricflow_engine import MetricFlowQueryRequest, MetricFlowQueryResult


class MockMetricFlowEngine:
    """Mock MetricFlowEngine class as only integration is needed to be tested."""

    def query(self, mf_request: MetricFlowQueryRequest) -> MetricFlowQueryResult:  # noqa: D
        data = {"metric1": [123, 5123, 23, 5123], "ds": [1, 2, 3, 4]}
        return MetricFlowQueryResult(
            query_spec=None,  # type: ignore
            dataflow_plan=None,  # type: ignore
            sql="SELECT * FROM hello",
            result_df=pd.DataFrame(data),
            result_table=None,
        )

    def dimensions_for_metrics(self, metric_names: List[str]) -> List[Dimension]:  # noqa: D
        dimensions = ["dim1", "dim2", "dim3"]
        return [Dimension(name) for name in dimensions]

    def list_metrics(self) -> List[Metric]:  # noqa: D
        return [Metric(name="metric1", dimensions=self.dimensions_for_metrics(metric_names=[]))]

    def get_dimension_values(  # noqa: D
        self,
        metric_name: str,
        get_group_by_values: str,
        time_constraint_start: Optional[datetime.datetime] = None,
        time_constraint_end: Optional[datetime.datetime] = None,
    ) -> List[str]:
        return ["dim_val1", "dim_val2", "dim_val3"]

    def list_materializations(self) -> List[Materialization]:  # noqa: D
        return [Materialization(name="mat1", metrics=["metric1"], dimensions=["dim1", "dim2"], destination_table=None)]


class MetricFlowCliRunner(CliRunner):
    """Custom CliRunner class to handle mocks."""

    def run(self, cli: click.BaseCommand, args: Sequence[str] = None) -> Result:  # noqa: D
        # Mock the metricflow engine
        cli_context = CLIContext()
        cli_context._mf = MockMetricFlowEngine()  # type: ignore
        return super().invoke(cli, args, obj=cli_context)


@pytest.fixture
def cli_runner() -> MetricFlowCliRunner:  # noqa: D
    return MetricFlowCliRunner()
