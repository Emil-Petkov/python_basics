def convert_usd_to_bgn(usd: float):
    fixed_rate = 1.79549

    return usd * fixed_rate


usd = float(input())
print(convert_usd_to_bgn(usd))
