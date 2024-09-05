text = "The sun dipped below the horizon, painting the sky in shades of pink and orange. As twilight settled, the first stars began to appear, twinkling faintly against the deepening blue. The evening air grew cooler, carrying the soft scent of blooming flowers and fresh earth. It was a tranquil moment, inviting all who witnessed it to pause and reflect."

list_result = [i for i in text.split(' ')]
set_result = set(list_result)
sort_result = sorted(set_result)

print(f'Your paragraph word list is: {list_result}')
print(f'Your set of word with unique value are: {set_result}')
print(f'Your sorted set of word list is: {sort_result}')