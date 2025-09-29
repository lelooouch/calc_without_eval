def check_winners(scores, student_score):
    scores.sort(reverse=True)
    for i in range(3):
        if student_score == scores[i]:
            return "Вы в тройке победителей!"
    return "Вы не попали в тройку победителей."




scores = input("Введите баллы через запятую:").split(', ')
student_score = str(input("Баллы Стаса:"))
print(check_winners(scores, student_score))
