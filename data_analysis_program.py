# this program is used to get the statistics for different personality types

from collections import Counter
from pandas import read_csv

FILENAME = "shipping_chart.csv"

df = read_csv(FILENAME, comment="#")
types = list(df.columns)[1:]

def print_dict(dictionary):
    for type, values in dictionary.items():
        print(type, values)
    print("")

results_sum_for_each_type = dict()
for type in types:
    type_results = [0,0,0,0,0,0,0]
    for data_point in df[type]:
        data_point = list(map(int, data_point.split(';')))
        for i in range(7):
            type_results[i] += data_point[i]
    results_sum_for_each_type[type] = type_results

print_dict(results_sum_for_each_type)

participants = df[list(df.columns)[0]]
participation_count = Counter(participants)

print_dict(participation_count)

def character_count(character_index: int, 
                    option1: str, 
                    option2: str) -> dict:
    option_1_count = [0,0,0,0,0,0,0]
    option_2_count = [0,0,0,0,0,0,0]
    for type, values in results_sum_for_each_type.items():
        if type[character_index] == option1:
            for i in range(7):
                option_1_count[i] += values[i]
        else:
            for i in range(7):
                option_2_count[i] += values[i]
    return {option1: option_1_count,
            option2: option_2_count}

preference_i_e = character_count(0, "I", "E")
preference_n_s = character_count(1, "N", "S")
preference_t_f = character_count(2, "T", "F")
preference_p_j = character_count(3, "P", "J")

print_dict(preference_i_e)
print_dict(preference_n_s)
print_dict(preference_t_f)
print_dict(preference_p_j)