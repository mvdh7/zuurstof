# %%
import numpy as np

import zuurstof as zs


def test_saturation():
    rng = np.random.default_rng()
    npts = (1000, 5, 3)
    ts = {
        "temperature": rng.uniform(-1, 40, size=npts),
        "salinity": rng.uniform(0, 42, size=npts),
    }
    o2sat = zs.o2_saturation(**ts)
    aou = zs.aou(o2sat, **ts)
    aou_percent = zs.aou_percent(o2sat, **ts)
    aou_zero = zs.aou(0, **ts)
    assert np.allclose(aou, 0)
    assert np.allclose(aou_percent, 0)
    assert np.allclose(o2sat, aou_zero)


# test_saturation()
