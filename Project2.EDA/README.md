# Проект по EDA "Экзамент по математике"

### Общая идея (контекст нашей задачи)
Отследить влияние условий жизни учащихся в возрасте от 15 
до 22 лет на их успеваемость по математике, чтобы на ранней 
стадии выявлять студентов, находящихся в группе риска.


### Цели текущего этапа проекта (наша задача)
Провести первичную обработку данных (анализ, очистка и подготовка данных для будущей модели).

### Этапы работы над проектом
1. Первичная обработка данных. Написать функции, которые можно применять к столбцам определённого типа.
2. Посмотреть на распределение признака для числовых переменных, устранить выбросы.
3. Оценить количество уникальных значений для номинативных переменных. По необходимости преобразовать данные.
4. Провести корреляционный анализ количественных переменных. Отобрать некоррелирующие переменные.
5. Проанализировать номинативные переменные и устранить те, которые не влияют на предсказываемую величину.
6. Сформулировать выводы относительно качества данных и тех переменных, которые будут отобраны для дальнейших построений модели.

### Краткая информация о данных 
1. school — аббревиатура школы, в которой учится ученик
2. sex — пол ученика ('F' - женский, 'M' - мужской)
3. age — возраст ученика (от 15 до 22)
4. address — тип адреса ученика ('U' - городской, 'R' - за городом)
5. famsize — размер семьи('LE3' <= 3, 'GT3' >3)
6. Pstatus — статус совместного жилья родителей ('T' - живут вместе 'A' - раздельно)
7. Medu — образование матери (0 - нет, 1 - 4 класса, 2 - 5-9 классы, 3 - среднее специальное или 11 классов, 4 - высшее)
8. Fedu — образование отца (0 - нет, 1 - 4 класса, 2 - 5-9 классы, 3 - среднее специальное или 11 классов, 4 - высшее)
9. Mjob — работа матери ('teacher' - учитель, 'health' - сфера здравоохранения, 'services' - гос служба, 'at_home' - не работает, 'other' - другое)
10. Fjob — работа отца ('teacher' - учитель, 'health' - сфера здравоохранения, 'services' - гос служба, 'at_home' - не работает, 'other' - другое)
11. reason — причина выбора школы ('home' - близость к дому, 'reputation' - репутация школы, 'course' - образовательная программа, 'other' - другое)
12. guardian — опекун ('mother' - мать, 'father' - отец, 'other' - другое)
13. traveltime — время в пути до школы (1 - <15 мин., 2 - 15-30 мин., 3 - 30-60 мин., 4 - >60 мин.)
14. studytime — время на учёбу помимо школы в неделю (1 - <2 часов, 2 - 2-5 часов, 3 - 5-10 часов, 4 - >10 часов)
15. failures — количество внеучебных неудач (n, если 1<=n<3, иначе 4)
16. schoolsup — дополнительная образовательная поддержка (yes или no)
17. famsup — семейная образовательная поддержка (yes или no)
18. paid — дополнительные платные занятия по математике (yes или no)
19. activities — дополнительные внеучебные занятия (yes или no)
20. nursery — посещал детский сад (yes или no)
21. higher — хочет получить высшее образование (yes или no)
22. internet — наличие интернета дома (yes или no)
23. romantic — в романтических отношениях (yes или no)
24. famrel — семейные отношения (от 1 - очень плохо до 5 - очень хорошо)
25. freetime — свободное время после школы (от 1 - очень мало до 5 - очень мого)
26. goout — проведение времени с друзьями (от 1 - очень мало до 5 - очень много)
27. health — текущее состояние здоровья (от 1 - очень плохо до 5 - очень хорошо)
28. absences — количество пропущенных занятий
29. score — баллы по госэкзамену по математике

### Файлы проекта
- stud_math.csv - исходный датасет
- stud_math_after_EDA.csv - датасет после EDA
- DST-10_Project2_Arcis_EDA.ipynb - ноутбук с проектом (EDA)
- my_lib_rds2.py - модуль с функциями к данному проекту
