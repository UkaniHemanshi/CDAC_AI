i_list = [x for x in range(1,21)]
output_list = ["FizzBuzz" if i_list[i] % 3 == 0 and i_list[i] % 5 == 0 else "Buzz" if i_list[i] % 5 == 0 else "Fizz" if i_list[i] % 3 == 0 else i_list[i] for i in range(len(i_list))]
print(output_list)