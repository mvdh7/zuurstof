# %%
import pandas as pd

import zuurstof as zs


def test_read_cary_oxygen():
    samples = zs.read_cary_oxygen("tests/data/samples.csv")
    assert isinstance(samples, pd.DataFrame)
    assert samples.shape == (100, 8)
    standards = zs.read_cary_oxygen("tests/data/standards.csv")
    assert isinstance(standards, pd.DataFrame)
    assert standards.shape == (40, 8)


# test_read_cary_oxygen()
