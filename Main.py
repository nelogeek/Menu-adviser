# -*- coding: utf-8 -*-
import re

# Меню
first_meal = [
    ['1', 'Чао Пин', 239],
    ['2', 'Грибной крем-суп', 179],
    ['3', 'Солянка', 149],
    ['4', 'Борщ', 139]
]

second_meal = [
    ['1', 'Свинина по-французски', 349],
    ['2', 'Паста с курой и грибами', 219],
    ['3', 'Лосось по-норвежски', 499],
    ['4', 'Равиоли с белой рыбой', 289]
]

drink = [
    ['1', 'Облепиховый морс', 99],
    ['2', 'Heineken', 149],
    ['3', 'Латте макиато', 129],
    ['4', 'Летний пунш', 229]
]

if __name__ == "__main__":

    print('Первые блюда:', end='\n')
    for i in first_meal:
        print(f"{i[0]}. {i[1]} - {i[2]}")
    print('Вторые блюда:', end='\n')
    for i in second_meal:
        print(f"{i[0]}. {i[1]} - {i[2]}")
    print('Напитки:', end='\n')
    for i in drink:
        print(f"{i[0]}. {i[1]} - {i[2]}")

    while True:# проверка на правильность ввода типов блюд
        print('Введите, пожалуйста, какие наборы типов блюд вы хотите съесть: '
              'например, "первое, напиток" или "первое, второе, напиток"', end='\n')
                # ЧёрныйRollsRoyceЗабираетДжекПот
        answer_meal = re.findall(r'\w+', input().lower())# находит все слова
        if "первое" in answer_meal or "второе" in answer_meal or "напиток" in answer_meal:
            break

    print('Введите, пожалуйста, сумму, которую вы готовы потратить на обед: например, "850 рублей"', end='\n')
    answer_sum = int(re.findall(r'\d+', input())[0])# находит все числа и выводит первое по списку число
    #ЧёрныйRollsRoyceЗабираетДжекПот

    if "первое" in answer_meal and "второе" in answer_meal and "напиток" in answer_meal:
        meal_sum = 0
        meal_name = ''
        for i in first_meal:
            for j in second_meal:
                for k in drink:
                    if meal_sum < j[2] + i[2] + k[2] < answer_sum:
                        meal_sum = j[2] + i[2] + k[2]
                        meal_name = f'{i[1]}, {j[1]}, {k[1]}'
                    a.append
        if meal_name:
            print(f'{meal_name} - {meal_sum} руб.', end='\n')
            print(f'Ваша сдача: {answer_sum - meal_sum} руб.', end='\n')
        else:
            print(f'Сумма слишком маленькая', end='\n')

    elif "первое" in answer_meal and "второе" in answer_meal:
        meal_sum = 0
        meal_name = ''
        for i in second_meal:
            for j in first_meal:
                if meal_sum < j[2] + i[2] < answer_sum:
                    meal_sum = j[2] + i[2]
                    meal_name = f'{j[1]}, {i[1]}'
        if meal_name:
            print(f'{meal_name} - {meal_sum} руб.', end='\n')
            print(f'Ваша сдача: {answer_sum - meal_sum} руб.', end='\n')
        else:
            print(f'Сумма слишком маленькая', end='\n')
        

    elif "второе" in answer_meal and "напиток" in answer_meal:
        meal_sum = 0
        meal_name = ''
        for i in second_meal:
            for j in drink:
                if meal_sum < j[2] + i[2] < answer_sum:
                    meal_sum = i[2] + j[2]
                    meal_name = f'{i[1]}, {j[1]}'
        if meal_name:
            print(f'{meal_name} - {meal_sum} руб.', end='\n')
            print(f'Ваша сдача: {answer_sum - meal_sum} руб.', end='\n')
        else:
            print(f'Сумма слишком маленькая', end='\n')

    elif "первое" in answer_meal and "напиток" in answer_meal:
        meal_name = ''
        meal_sum = 0# пример данных: [['Облепиховый морс и Чао Пин', 338],
        for i in first_meal:# ['Heineken и Чао Пин', 388], ['Латте макиато и Чао Пин', 368] и т.д
            for j in drink:# потом находится наибольшая сумма, которая не превышает answer_sum... согласен, алгоритм ужасный, но зато рабочий
                if meal_sum < j[2]+i[2] < answer_sum:
                    meal_sum = j[2]+i[2]
                    meal_name = f'{i[1]}, {j[1]}'
        if meal_name:
            print(f'{meal_name} - {meal_sum} руб.', end='\n')
            print(f'Ваша сдача: {answer_sum-meal_sum} руб.', end='\n')
        else:
            print(f'Сумма слишком маленькая', end='\n')

    elif "первое" in answer_meal:
        meal_sum = 0
        meal_name = ''
        for i in first_meal:
            if meal_sum <= i[2] <= answer_sum:
                meal_sum = i[2]
                meal_name = i[1]
        if meal_name:
            print(f'{meal_name} - {meal_sum} руб.', end='\n')
            print(f'Ваша сдача: {answer_sum - meal_sum} руб.', end='\n')
        else:
            print(f'Сумма слишком маленькая', end='\n')

    elif "второе" in answer_meal:
        meal_sum = 0
        meal_name = ''
        for i in second_meal:
            if meal_sum <= i[2] <= answer_sum:
                meal_sum = i[2]
                meal_name = i[1]
        if meal_name:
            print(f'{meal_name} - {meal_sum} руб.', end='\n')
            print(f'Ваша сдача: {answer_sum - meal_sum} руб.', end='\n')
        else:
            print(f'Сумма слишком маленькая', end='\n')

    elif "напиток" in answer_meal:
        meal_sum = 0
        meal_name = ''
        for i in drink:
            if meal_sum <= i[2] <= answer_sum:
                meal_sum = i[2]
                meal_name = i[1]
        if meal_name:
            print(f'{meal_name} - {meal_sum} руб.', end='\n')
            print(f'Ваша сдача: {answer_sum - meal_sum} руб.', end='\n')
        else:
            print(f'Сумма слишком маленькая', end='\n')

    else:
        print('К сожалению, такого нет в меню...', end='\n')

    change = answer_sum - meal_sum # сдача

    print('\nВот, что вы еще можете купить на сдачу:', end='\n')
    for i in first_meal:
        if i[2] <= change:
            print(f'{i[1]} - {i[2]} руб.', end='\n')

    for i in second_meal:
        if i[2] <= change:
            print(f'{i[1]} - {i[2]} руб.', end='\n')

    for i in drink:
        if i[2] <= change:
            print(f'{i[1]} - {i[2]} руб.', end='\n')


