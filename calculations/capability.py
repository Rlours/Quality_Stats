import numpy as np


def calculate_capability(data, lsl, usl):
    """
    Calculate basic process capability statistics.

    Parameters
    ----------
    data : list or array-like
        Process measurement data.
    lsl : float
        Lower Specification Limit.
    usl : float
        Upper Specification Limit.

    Returns
    -------
    dict
        Process statistics and capability indices.
    """

    data = np.asarray(data, dtype=float)

    # Remove missing values
    data = data[~np.isnan(data)]

    # Basic validation
    if len(data) < 2:
        raise ValueError("At least two measurements are required.")

    if usl <= lsl:
        raise ValueError("USL must be greater than LSL.")

    # Basic statistics
    n = len(data)
    mean = np.mean(data)

    # Sample standard deviation
    std_dev = np.std(data, ddof=1)

    minimum = np.min(data)
    maximum = np.max(data)

    # Capability
    cp = (usl - lsl) / (6 * std_dev)

    cpu = (usl - mean) / (3 * std_dev)

    cpl = (mean - lsl) / (3 * std_dev)

    cpk = min(cpu, cpl)

    return {
        "n": n,
        "mean": mean,
        "std_dev": std_dev,
        "minimum": minimum,
        "maximum": maximum,
        "cp": cp,
        "cpu": cpu,
        "cpl": cpl,
        "cpk": cpk,
    }