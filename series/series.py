def slices(series, longitud):
    if not 1 <= longitud <= len(series):
        raise ValueError("Invalid slice length for this series: " + str(
            longitud))
    return [series[i:i + longitud] for i in range(len(series) - longitud + 1)]
