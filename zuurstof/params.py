import numpy as np

from .meta import warn


def o2_saturation(temperature=25, salinity=35):
    """Calculate saturated dissolved oxygen in µmol/kg-sw,
    using the "combined-fit" constants of García & Gordon (1992, 1993).

    Valid for
      - freezing point <= temperature <= 40 °C, and
      - 0 <= salinity <= 42.

    References
    ----------
    García, H.E., and Gordon, L.I. (1992)
        Oxygen solubility in seawater: better fitting equations.
        Limnology and Oceanography, 37(6), 1307-1312.
        https://doi.org/10.4319/lo.1992.37.6.1307
    García, H.E., and Gordon, L.I. (1993)
        Erratum: Oxygen solubility in seawater: better fitting equations.
        Limnology and Oceanography, 38(3), 656.
        https://doi.org/10.4319/lo.1993.38.3.0643

    Parameters
    ----------
    temperature : float, optional
        Temperature in °C, by default 25.
    salinity : float, optional
        Practical salinity, by default 35.

    Returns
    -------
    float
        Saturated [O2] in µmol/kg-sw.
    """
    if np.any(temperature > 40):
        warn(
            "Some temperature values are greater than 40 °C, "
            + "which is the maximum value for the parameterisation"
        )
    if np.any(salinity > 42):
        warn(
            "Some salinity values are greater than 42, "
            + "which is the maximum value for the parameterisation"
        )
    # Define coefficients
    A0 = 5.80818
    A1 = 3.20684
    A2 = 4.11890
    A3 = 4.93845
    A4 = 1.01567
    A5 = 1.41575
    B0 = -0.00701211
    B1 = -0.00725958
    B2 = -0.00793334
    B3 = -0.00554491
    C0 = -0.000000132412
    # Scaled temperature
    ts = np.log((298.15 - temperature) / (273.15 + temperature))
    # Calculate saturated oxygen
    return np.exp(
        A0
        + A1 * ts
        + A2 * ts**2
        + A3 * ts**3
        + A4 * ts**4
        + A5 * ts**5
        + salinity * (B0 + B1 * ts + B2 * ts**2 + B3 * ts**3)
        + C0 * salinity**2
    )


def aou(oxygen, temperature=25, salinity=35):
    """Calculate apparent oxygen utilisation (AOU) in µmol/kg-sw,
    using the "combined-fit" constants of García & Gordon (1992, 1993).

    Valid for
      - freezing point <= temperature <= 40 °C, and
      - 0 <= salinity <= 42.

    References
    ----------
    García, H.E., and Gordon, L.I. (1992)
        Oxygen solubility in seawater: better fitting equations.
        Limnology and Oceanography, 37(6), 1307-1312.
        https://doi.org/10.4319/lo.1992.37.6.1307
    García, H.E., and Gordon, L.I. (1993)
        Erratum: Oxygen solubility in seawater: better fitting equations.
        Limnology and Oceanography, 38(3), 656.
        https://doi.org/10.4319/lo.1993.38.3.0643

    Parameters
    ----------
    oxygen : float
        Dissolved oxygen in µmol/kg-sw.
    temperature : float, optional
        Temperature in °C, by default 25.
    salinity : float, optional
        Practical salinity, by default 35.

    Returns
    -------
    float
        Apparent oxygen utilisation (AOU) in µmol/kg-sw.
    """
    o2sat = o2_saturation(temperature=temperature, salinity=salinity)
    return o2sat - oxygen


def aou_percent(oxygen, temperature=25, salinity=35):
    """Calculate apparent oxygen utilisation (AOU) as a percentage of
    dissolved oxygen substance content at saturation,
    using the "combined-fit" constants of García & Gordon (1992, 1993).

    Valid for
      - freezing point <= temperature <= 40 °C, and
      - 0 <= salinity <= 42.

    References
    ----------
    García, H.E., and Gordon, L.I. (1992)
        Oxygen solubility in seawater: better fitting equations.
        Limnology and Oceanography, 37(6), 1307-1312.
        https://doi.org/10.4319/lo.1992.37.6.1307
    García, H.E., and Gordon, L.I. (1993)
        Erratum: Oxygen solubility in seawater: better fitting equations.
        Limnology and Oceanography, 38(3), 656.
        https://doi.org/10.4319/lo.1993.38.3.0643

    Parameters
    ----------
    oxygen : float
        Dissolved oxygen in µmol/kg-sw.
    temperature : float, optional
        Temperature in °C, by default 25.
    salinity : float, optional
        Practical salinity, by default 35.

    Returns
    -------
    float
        Apparent oxygen utilisation (AOU) in %.
    """
    o2sat = o2_saturation(temperature=temperature, salinity=salinity)
    return 100 * (o2sat - oxygen) / o2sat
