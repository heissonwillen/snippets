with open('my_submission.csv', 'r') as my_sub:
    my_lines = my_sub.readlines()

with open('sub_titanic.csv', 'r') as feedback_sub:
    feedback_lines = feedback_sub.readlines()

diff = 0
for index, (my_line, feedback_line) in enumerate(zip(my_lines, feedback_lines)):
    if my_line != feedback_line:
        diff += 1
        print(my_line, feedback_line, end='')
        print(f'linha: {index}')


print(1-diff/len(my_lines))


# a = [1, 2, 3]
# b = [2, 5, 6]

# zip(a, b)
# [(1, 2), (2, 5), (3, 6)]
