from functools import reduce

def execute_aggregation_value():
    def doSum(x1, x2):
        return x1 + x2
    aggregation_value = reduce(doSum, number_list)
    print(aggregation_value)

number_list = [-5,200,300,-10,10,1000]
filtered_numbers = list(filter(lambda x: x > 100, number_list))
print(filtered_numbers)
transformation_numbers = list(map(lambda x:x ** 2, number_list))
print(transformation_numbers)
execute_aggregation_value()