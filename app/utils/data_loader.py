from snowflake.snowpark.context import get_active_session


def load_housing_data():
    session = get_active_session()

    return session.table(
        "ML_WORKFLOW_DB.ML_SCHEMA.HOUSING"
    ).to_pandas()