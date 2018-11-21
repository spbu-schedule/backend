import os

import matplotlib
matplotlib.use('Agg')

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings

warnings.simplefilter('ignore')
from pylab import rcParams

rcParams['figure.figsize'] = 8, 5

import time


def convert(x):
    x = x.tm_wday
    if x == 0:
        return 'пн'
    elif x == 1:
        return 'вт'
    elif x == 2:
        return 'ср'
    elif x == 3:
        return 'чт'
    elif x == 4:
        return 'пт'
    elif x == 5:
        return 'сб'


def weekNumber(x):
    return time.strftime("%W", time.strptime(x, "%Y-%m-%d"))


def preparation():
    df = pd.read_csv('data.csv', sep='~', encoding='utf-8',
                     usecols=['ContingentUnitCourse', 'ContingentUnitName', 'DivisionsString', 'DivisionName', 'Start',
                              'End', 'EducatorAssignment', 'LocationsDisplayText', 'Subject'])
    df.columns = ['Start', 'End', 'Курс', 'Номер группы', 'Факультет1', 'Факультет2', 'Преподаватель', 'Адрес',
                  'Предмет']
    df['Вид занятия'] = df['Предмет'].str.split(',').str.get(1)
    df['Предмет'] = df['Предмет'].str.split(',').str.get(0)
    df['День'] = df['Start'].str.split(' ').str.get(0)
    df['Время начала'] = df['Start'].str.split(' ').str.get(1)
    df['Время окончания'] = df['End'].str.split(' ').str.get(1)
    df['Факультет'] = df['Факультет1'].fillna(df['Факультет2'])
    df['День недели'] = (df['День'].apply(time.strptime, args=('%Y-%m-%d',))).apply(convert)
    df['Day'] = df['День'].apply(time.strptime, args=('%Y-%m-%d',))
    df['Номер недели'] = df['День'].apply(weekNumber)
    df = df[
        ['Номер группы', 'Факультет', 'Курс', 'Преподаватель', 'Адрес', 'Предмет', 'Вид занятия', 'День', 'День недели',
         'Номер недели', 'Время начала', 'Время окончания']]
    df = pd.concat([df[df['День недели'] == 'пн'], df[df['День недели'] == 'вт'], df[df['День недели'] == 'ср'],
                    df[df['День недели'] == 'чт'], df[df['День недели'] == 'пт'], df[df['День недели'] == 'сб']],
                   ignore_index=True)
    plt.clf()
    return df


# -----------------------------------------------------------------------------------

# Список преподавателей, обучающих выбранную группу
def tool_2_1_1(faculty, number):
    df = preparation()
    return  pd.unique(df[(df['Номер группы'] == number) & (df['Факультет'] == faculty)]['Преподаватель'])


# Список преподавателей, ведущих выбранную дисциплину
def tool_2_1_2(faculty, lesson):
    df = preparation()
    return pd.unique(df[(df['Предмет'] == lesson) & (df['Факультет'] == faculty)]['Преподаватель'])


# Занятость преподавателей, обучающих выбранную группу
def tool_2_2_1(faculty, number):
    name = 'tool_2_2_1,' + faculty + ',' + number + '.svg'
    if os.path.isfile('./mainApp/static/' + name):
        return name
    df = preparation()
    sns.countplot(df[(df['Факультет'] == faculty) & (df['Номер группы'] == number)]['Преподаватель'])
    plt.ylabel('Количество пар')
    plt.title('Загруженность преподавателей')
    plt.xticks(rotation=90)
    plt.savefig('./mainApp/static/' + name)
    return name


# Занятость преподавателей, ведущих выбранную дисциплину
def tool_2_2_2(faculty, lesson):
    name = 'tool_2_2_2,' + faculty + ',' + lesson + '.svg'
    if os.path.isfile('./mainApp/static/' + name):
        return name
    df = preparation()
    sns.countplot(df[(df['Факультет'] == faculty) & (df['Предмет'] == lesson)]['Преподаватель'])
    plt.ylabel('Количество пар')
    plt.title('Загруженность преподавателей')
    plt.xticks(rotation=90)
    plt.savefig('./mainApp/static/' + name)
    return name


# Занятость определённых преподавателей
def tool_2_3(faculty, teacherName, day):
    name = 'tool_2_2_2,' + faculty + ',' + teacherName + ',' + day + '.svg'
    if os.path.isfile('./mainApp/static/' + name):
        return name
    df = preparation()
    week5 = time.strftime("%W", time.strptime(day, "%Y-%m-%d"))
    sns.countplot(
        df[(df['Преподаватель'] == teacherName) & (df['Факультет'] == faculty) & (df['Номер недели'] == week5)][
            'День недели'])
    plt.title('Количество пар для определенного преподавателя по дням недели')
    plt.savefig('./mainApp/static/'+name)
    return name

