def circumference(r):
    def perimeter_of_a_circle():
        length = round(float(2 * 3.14 * r), 2)
        print(length)
    return perimeter_of_a_circle


result = circumference(9.8)
result()