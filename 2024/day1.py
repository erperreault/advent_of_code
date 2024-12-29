from collections import defaultdict, Counter

# data = [line for line in open('test_data.txt')]
data = [line for line in open('real_data.txt')]

left_column, right_column = [], []
for line in data:
    left, right = (int(x) for x in line.split())
    left_column.append(left)
    right_column.append(right)
left_column, right_column = sorted(left_column), sorted(right_column)

total_distance = 0
for index in range(len(left_column)):
    total_distance += abs(left_column[index] - right_column[index])

print(total_distance)

###

left_column = []
right_column_counts = defaultdict(int)
for line in data:
    left, right = (int(x) for x in line.split())
    left_column.append(left)
    right_column_counts[right] += 1

similarity_score = 0
for i in left_column:
    if i in right_column_counts:
        similarity_score += i * right_column_counts[i]

print(similarity_score)

###

right_column_counts = Counter(right_column)

similarity_score = 0
for i in left_column:
    similarity_score += i * right_column_counts[i]

print(similarity_score)

