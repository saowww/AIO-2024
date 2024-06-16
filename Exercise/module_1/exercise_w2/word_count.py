def count_words(file_path):
    file = open(file_path, 'r')
    result = {}
    for line in file:
        words = line.split()
        for word in words:
            if word not in result:
                result[word] = 1
            else:
                result[word] = result[word] + 1
    return result


file_path = '/Users/maitiendung/git/AIO-2024/Exercise/module_1/exercise_w2/P1_data.txt'


result = count_words(file_path)
assert result['who'] == 3
print(result['man'])
