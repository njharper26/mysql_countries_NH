# 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)
select countries.name, language, percentage
from countries, languages
where countries.id = country_id and language = 'slovene'
order by percentage desc;

# 2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)
select countries.name, count(cities.name)
from countries, cities
where countries.id = country_id
group by country_code;

# 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)
select country_code, name, population
from cities
where country_id = 136 and population > 500000
order by population desc;

# 4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)
select countries.name, language, percentage
from languages, countries
where countries.id = country_id and percentage > 89.9
order by percentage desc

# 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
select name, surface_area, population
from countries
where surface_area < 501 and population > 100000
order by surface_area, population

# 6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)
select name, government_form, capital, life_expectancy
from countries
where government_form = 'constitutional monarchy' and capital > 200 and life_expectancy > 75

# 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
select countries.name, cities.name, district, cities.population
from countries, cities
where countries.id = country_id and district = 'buenos aires' and cities.population > 500000

# 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
select region, count(name) as '# of countries'
from countries
group by region
order by count(name) desc
