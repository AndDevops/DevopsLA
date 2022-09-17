
minutes = 12345678

minutes_in_a_year = 60* 24 *365

minutes_in_a_day = 60*24

total_number_of_years = minutes //  minutes_in_a_year

remaining_minutes_after_years  = minutes % minutes_in_a_year

total_days = remaining_minutes_after_years // minutes_in_a_day

print(f"{minutes} amount of minutes makes {total_number_of_years}years and {total_days}days")

