dict_score = {'Alice':85, 'Bob':92, 'Charlie':78, 'David':65}

result_dict = {key:value+5 for key,value in dict_score.items() if value > 80 }

print(f'Your resulting dictionary whose score is above 80: {result_dict}')