def population_growth(initial_pop, annual_growth_rate, target_pop):
    current_pop = initial_pop
    num_years_passed = 0
    if annual_growth_rate > 0:
        while current_pop <= target_pop:
            current_pop *= (1 + annual_growth_rate)
            num_years_passed += 1
        return num_years_passed
    return 'invalid growth rate'
