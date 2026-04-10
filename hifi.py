"""High-fidelity 1D signal utilities (linear interpolation resampling)."""

from __future__ import annotations

from collections.abc import Sequence


def resample_linear_1d(signal: Sequence[float], out_length: int) -> list[float]:
    """
    Resample a 1D signal to ``out_length`` samples using linear interpolation.

    This is a minimal building block for sample-rate conversion when combined
    with rational ``in_length / out_length`` ratios, and keeps amplitude
    bounded between adjacent input samples.

    Parameters
    ----------
    signal:
        Input samples. Empty input yields an empty list.
    out_length:
        Number of output samples. Non-positive values yield an empty list.

    Returns
    -------
    list[float]
        Resampled values, length ``out_length`` (or 0 for invalid inputs).

    Examples
    --------
    >>> resample_linear_1d([0.0, 1.0], 3)
    [0.0, 0.5, 1.0]
    >>> resample_linear_1d([42.0], 4)
    [42.0, 42.0, 42.0, 42.0]
    """
    if out_length <= 0 or len(signal) == 0:
        return []

    n = len(signal)
    if n == 1:
        v = float(signal[0])
        return [v] * out_length

    if out_length == 1:
        return [float(signal[0])]

    # Map output index j in [0, out_length - 1] to fractional index in [0, n - 1]
    scale = (n - 1) / (out_length - 1)
    out: list[float] = []
    for j in range(out_length):
        x = j * scale
        i0 = int(x)
        if i0 >= n - 1:
            out.append(float(signal[n - 1]))
            continue
        frac = x - i0
        a = float(signal[i0])
        b = float(signal[i0 + 1])
        out.append(a + frac * (b - a))
    return out
