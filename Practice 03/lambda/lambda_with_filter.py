# Using lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Second example 
quotes = [ "Қолда барда алтынның қадірі жоқ.",
            "Көп сөз көмір, аз сөз алтын.",
            "Ердің екі сөйлегені өлгені.",
            "Жақсы дос ашып айтар, жаман дос қосып айтар.",
            "Жеті рет өлшеп, бір рет кес.",
            "Адамды сыртынан емес, ішінен таны." ]
long_quotes = list(filter(lambda x: len(x) > 30, quotes))
print(long_quotes)


# Third example
students = [ {"name": "Yernar", "grade": 100},
             {"name": "Azamat", "grade": 92},
             {"name": "Orynbasar", "grade": 78},
             {"name": "Tasbolat", "grade": 90} ]
high_achievers = list(filter(lambda name: name["grade"] >= 90, students))
print(high_achievers)


# Fourth example
weekly_sales = [ {"product": "Laptop", "sales": 150},
                {"product": "Smartphone", "sales": 300},
                {"product": "Headphones", "sales": 80},
                {"product": "Tablet", "sales": 120} ]
top_sellers = list(filter(lambda item: item["sales"] > 150, weekly_sales))
print(top_sellers)

