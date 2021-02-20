city_name = "Instabul, Turkey"
pop_1927 = 691000
pop_2017 = 15029231
pop_1950 = 983000
pop_2000 = 8831800

pop_change = pop_2017 - pop_1927

percentage_gr = (pop_change/pop_1927) * 100

annual_gr = percentage_gr/(2017-1927)

def population_growth(year_one,year_two,population_one,population_two):
  pop_change = population_two - population_one
  percentage_gr = (pop_change/population_one) * 100
  growth_rate = percentage_gr/(year_two - year_one)
  return growth_rate
  
print(annual_gr)

set_one = population_growth(1927,2017,pop_1927,pop_2017)
print(set_one)

set_two = population_growth(1950,2000,pop_1950,pop_2000)
print(set_two)

report = f"The population of Istanbul grew from {pop_1927} to {pop_2017} for a total growth of {pop_change}. The annual growth rate during that time was {annual_gr}%."
print(report)