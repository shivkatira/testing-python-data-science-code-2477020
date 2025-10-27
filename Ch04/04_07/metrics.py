import pandas as pd
import pandera.pandas as pa
from pandera import check_output


def is_cpu_or_mem(text):
    cpu_mem = ["cpu", "mem"]
    if text in cpu_mem:
        return True
    return False


metrics_schema = pa.DataFrameSchema(
    {
        "time": pa.Column(pd.DatetimeTZDtype("ns", "UTC")),
        "metric": pa.Column(str, checks=pa.Check(is_cpu_or_mem, element_wise=True)),
        "value": pa.Column(pd.Float64Dtype, checks=pa.Check.greater_than(0)),
    }
)


@check_output(metrics_schema)
def load_metrics(jsonl_file):
    return pd.read_json(
        jsonl_file,
        orient="records",
        lines=True,
        convert_dates=["time"],
    )


# testing
if "__name__" == "__main__":
    from pathlib import Path

    here = Path(__file__).absolute().parent
    jsonl_file = here / "metrics.jsonl"

    df = load_metrics(jsonl_file)
    metrics_schema.validate(df)
