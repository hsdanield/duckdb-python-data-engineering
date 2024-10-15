from ingestion.bigquery import (
    get_bigquery_client,
    get_bigquery_result,
    build_pypi_query,
)
import os
from ingestion.models import (
    validate_dataframe,
    FileDownloads,
    PypiJobParameters,
)
import fire
import duckdb


def main(params: PypiJobParameters):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
        "/home/dhans/.config/gcloud/demo-pypi.json"
    )
    df = get_bigquery_result(
        query_str=build_pypi_query(params),
        bigquery_client=get_bigquery_client("dev-ws-bq"),
    )
    validate_dataframe(df, FileDownloads)
    conn = duckdb.connect()
    conn.sql(
        "COPY (SELECT * FROM df) TO 'duckdb.csv' (FORMAT csv, HEADER true)"
    )


if __name__ == "__main__":
    fire.Fire(lambda **kwargs: main(PypiJobParameters(**kwargs)))
