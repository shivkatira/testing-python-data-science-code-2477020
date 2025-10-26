import os

import numpy as np
import pytest
import yaml
from splitter import split_to_chunks


def load_testcases(input_file):
    if not os.path.exists(input_file):
        raise Exception("YAML file not found")
    with open(input_file, "r") as file:
        data = yaml.safe_load(file)
    return [list(d.values()) for d in data]


root = os.path.dirname(os.path.abspath("__file__"))
input_file = os.path.join(root, "Ch02", "02_06", "split_cases.yml")
test_cases = load_testcases(input_file)


def test_split_to_chunks_exists():
    split_to_chunks(10, 3)


@pytest.mark.parametrize("size, chunksize, chunks", test_cases)
def test_split_to_chunks(size, chunksize, chunks):
    out = split_to_chunks(size, chunksize)
    assert np.allclose(list(out), [tuple(l) for l in chunks])
