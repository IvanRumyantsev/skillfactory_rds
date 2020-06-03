def percent(a,c):
    '''Выражаем в процентах первое число относительно второго'''
    result = str(round(a/c*100,1)) + '%'
    return result

def outliers(s, k = 1.5):
    '''
    Определяем выбросы сверху (top) и снизу (down) в наборе данных
    по межквартиьному интервалу. Есть возможность изменять межквартильный интервал
    через коэффициент k. 
    '''
    import pandas as pd
    
    median = s.median()
    IQR = s.quantile(0.75) - s.quantile(0.25)
    Q1 = s.quantile(0.25)
    Q3 = s.quantile(0.75)
    top = Q3 + k*IQR
    down = Q1 - k*IQR
    out_top = s[s > top]
    out_down = s[s < down]

    print('Нижняя граница: ', down, ' и таких значений ', len(out_down))
    print('Верхняя граница: ', top, ' и таких значений ', len(out_top))
    return

def miss_count(df, col_names = None):
    import pandas as pd
    
    if col_names == None:
        col_names = list(df.columns)
    
    rows = len(df)
    miss_df = pd.DataFrame()
    miss_df['col'] = col_names
    miss_df['miss'] = [len(df[df[col].isnull()]) for col in col_names]
    miss_df['percent'] = miss_df.miss.apply(lambda x: round(x/rows*100,1))
    miss_df['nunique'] = [df[col].nunique() for col in col_names]
    
    return miss_df

def hist_and_box(df_column):
    '''
    Вывод гистограммы и боксплота в один ряд.
    На входе объект pd.Series
    Автор: https://github.com/Carbophozz
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    bins= len(df_column.value_counts())
    fig = plt.figure(figsize=(12, 4)) 
    ax_1 = fig.add_subplot(121)
    ax_1.set_xlabel(df_column.name)
    df_column.hist(bins=bins, ax=ax_1)
    sns.boxplot(df_column, ax=fig.add_subplot(122))
    plt.show()
    return None

def fill_by_prop(df, col):
    '''
    Заполняем данные с пропусками рандомно 
    в той же пропорции что и имеющиеся данные.
    '''
    from random import random
    import pandas as pd
    miss_ind = df[df[col].isnull()].index
    # вычисляем значения функции распределения
    prop = df[col].value_counts(normalize=True, ascending=True, dropna=True).cumsum()
    
    # подставляем соответствующее случайной величине от 0 до 1 значение из таблицы
    fill_na = df.loc[miss_ind][col].apply(lambda x: prop[prop >= random()].idxmin())
    
    return fill_na

def mode_change(df, A, B):
    '''
    Заменяет пропуски в столбце A на самые частотные в соотвествии со столбцом B.
    Например a15 = None, находим самое частотное значение в столбце A для значений b15.
    Если b5 = None, то то самое частотное значение среди всех значений A.
    '''
    
    
    # находим уникальные значения в столбце B
    keys = list(df[B].value_counts().index)
    
    #создаём словарь где ключ это уникальное значение из столбца B, а значение - мода по столбцу А
    dict_mode = {}
    for key in keys:
        dict_mode[key] = df[df[B] == key][A].mode()[0]

    #найдём моду в B
    mode_B = df[B].mode()[0]    
        
    #разбираемся с пропусками в А, где в B пропусков нет
    index_1 = [x[0] for x in df[(df[A].isnull())&(df[B].notnull())].iterrows()]
         
    for i in index_1:
        print(i, df.loc[i, A],' -> ', dict_mode[df[B][i]])
        df.loc[i, A] = dict_mode[df[B][i]]
    
    #разбираемся с пропусками в А, где в B пропуски
    index_2 = [x[0] for x in df[(df[A].isnull())&(df[B].isnull())].iterrows()]
    for i in index_2:
        print(i, df.loc[i, A],' -> ', dict_mode[mode_B])
        df.loc[i, A] = dict_mode[mode_B]


def get_stat_dif(df, column, score):
    '''
        Функция для проверки статистической разницы в распределении оценок по номинативным признакам
    с помощью теста Стьюдента встроенного в функцию ttest_ind().
        На входе имеем имя столбца с неколичественными (номинативными) данными.
        Проверяем характер распределения оценок в зависимости от значений в этом столбце.
    '''
    from scipy.stats import ttest_ind
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from itertools import combinations
    from scipy.stats import ttest_ind
    
    # Выбираем 10 самых частотных варианта для текущего столбца
    cols = df.loc[:, column].value_counts().index #[:10] 
    
    # Создаём все возможные парные комбинации из элементов списка cols 
    # Например пара компаний:'Soma', 'Fresco'
    combinations_all = list(combinations(cols, 2))
    
    # Для каждой пары номинативных значений рассматриваемого столбца
    # выполняем тест Стьюдента с поправкой Бонферони
    for comb in combinations_all:
                
        # Готовим аргументы для функции ttest_ind()
        argument0 = df.loc[df.loc[:, column] == comb[0], score] #Например: оценки по продукции компании 'Soma'
        argument1 = df.loc[df.loc[:, column] == comb[1], score] #Например: оценки по продукции компании 'Fresco'
        
        
        if ttest_ind(argument0, argument1, nan_policy = 'omit').pvalue <= 0.05/len(combinations_all): # Учли поправку Бонферони
            
            # Выводим наименования интересующих нас столбцов
            print('Походу столбец ', score,' взаимосвязан со столбцом ', column)
            break

def change_this(column, arg1, arg2): # ВЕЛОСИПЕД!!!!!!!!!!!!!!!
    ''' Точечная замена значения arg1 на arg2.
    '''
    df[column] = df[column].apply(lambda x: arg2 if x == arg1  
                                   else x                          
                                  )
    
def nn(column):
    '''
    Замена некорректных данных на None
    '''
    df[column] = df[column].apply(lambda x: 
                                  None if pd.isnull(x)            # заменяем все виды нулей на None
                                  else None if x == 'nan'         # заменяем nan на None   
                                  else x                          # остальное оставляем как есть
                                  )