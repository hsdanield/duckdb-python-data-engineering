
include .env
export 

.PHONY: pypi-ingest format

pypi-ingest:
	poetry run python3 -m ingestion.pipeline \
		--start_date $$START_DATE \
		--end_date $$END_DATE \
		--pypi_project $$PYPI_PROJECT \
		--database_name $$DATABASE_NAME \
		--s3_path $$S3_PATH \
		--aws_profile $$AWS_PROFILE \
		--gcp_project $$GCP_PROJECT \
		--timestamp_column $$TIMESTAMP_COLUMN \
		--destination $$DESTINATION

format:
	ruff format .

pypi-ingest-test:
	pytest tests/ingestion

