def usd_to_bgn(n_dollars: float):
    current_rate_of_leva_to_the_dollar = 1.79549

    calculate = n_dollars * current_rate_of_leva_to_the_dollar

    return calculate


usd_dollar = float(input())

print(usd_to_bgn(usd_dollar))
