def total_unique_count(country):
    return len(country)

country = set()
total_country = int(input())
for i in range(1,total_country+1, 1):
    stamp = input()
    country.add(stamp)

print(total_unique_count(country))