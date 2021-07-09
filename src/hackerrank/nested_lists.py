records = [["Harsh", 20], ["Beria", 20], ["Varun", 19], ["Kakunami", 19], ["Vikas", 21]]

scores = list()
for record in records:
    scores.append(record[1])
print(scores)

minimum_score = min(scores)
print(minimum_score)
new_score_list = list()
for score in scores:
    if score != minimum_score:
        new_score_list.append(score)
print(new_score_list)
second_minimum_score = min(new_score_list)

list_of_names_with_minimum_score = list()
for record in records:
    if record[1] == second_minimum_score:
        list_of_names_with_minimum_score.append(record[0])

print(sorted(list_of_names_with_minimum_score))