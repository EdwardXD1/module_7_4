team1 = 'Мастера кода'
team2 = 'Волшебники данных'
def num(team1_n=0, team2_n=0):
    print('В команде %s участников: %s !' % (team1, team1_n))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_n, team2_n))

score1 = 0
score2 = 0
def time(team1_t=0, team2_t=0, tasks_total=0):
    time1 = team1_t
    time2 = team2_t
    print('Команда {} решила задач: {}!'.format(team2, score2))
    print('{} решили задачи за {} cек. !'.format(team2, time2))
def challenge_result(tasks_total=0, time_avg=0):
    print(f'Команды решили {score1} и {score2} задач')
    if score1 > score2:
        print(f'Результат битвы: победа команды {team1} !')
    else:
        print(f'Результат битвы: победа команды {team2} !')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')
num(team1_n=5, team2_n=6)
score1 = 40
score2 = 42
time(team1_t=1552.512, team2_t=2153.31451)
challenge_result(tasks_total=82, time_avg=45.2)