print('Приветствую, путник! По приказу короля ты должен победить колдуна. Чтобы добраться до колдуна тебе нужно пройти через лес, попасть в город и вдали ты увидишь замок колдуна. Для победы тебе понадобятся предметы: крестик, святая вода, осиновый кол. Удачи!')
print('Вы отправились в путь. Когда вы дошли до леса, стемнело. На опушке стоял дом. У вас есть выбор:')
print('Переночевать')
print('Пойти дальше')
b = 0
k = 0
a = ''
while b != 1:
    while a != 'Переночевать' and a != 'Пойти дальше':
        a = input()
        if a != 'Переночевать' and a != 'Пойти дальше':
            print('Нужно написать "Переночевать" или "Пойти дальше" (без кавычек).')
    if a == 'Переночевать':
        print('Вы постучали в дверь. Вам открыли. С улыбкой добродушной старик вас пустил.')
        print('- Могу я переночевать у вас? - спросили вы.')
        print('- Да. Будь как дома, путник. Я  ни в чём не откажу. Множество историй, коль желаешь, расскажу, - ответил вам старик.')
        print('Вы узнали, что этот старик - лесник и он любит подкармливать волков.')
        print('Среди ночи завыли волки под окном. Старик покидает дом.')
        print('У вас есть выбор:')
        print('Сбежать')
        print('Остаться')
        while a != 'Сбежать' and a != 'Остаться':
            a = input()
            if a != 'Сбежать' and a != 'Остаться':
                print('Нужно написать "Сбежать" или "Остаться" (без кавычек).')
        if a == 'Сбежать':
            print('Вы решаете сбежать. Пока вы шли по лесу, наступает рассвет. Вы доходите до города.')
        elif a == 'Остаться':
            print('Вы решаете остаться. Спустя небольшое время возвращается старик с ружьём наперевес.')
            print('- Друзья хотят покушать, пойдём, приятель, в лес! - сказал старик.')
            print('Вас убили.')
            k = 1
            break
    elif a == 'Пойти дальше':
        print('Вы решаете пойти дальше. По пути вы встречаете человека в чёрном цилиндре, в наряде старинном, а в руке была маска. У вас есть выбор:')
        print('Спросить дорогу в город')
        print('Пройти мимо')
        while a != 'Спросить дорогу в город' and a != 'Пройти мимо':
            a = input()
            if a != 'Спросить дорогу в город' and a != 'Пройти мимо':
                print('Нужно написать "Спросить дорогу в город" или "Пройти мимо" (без кавычек).')
        if a == 'Спросить дорогу в город':
            print('- Как мне попасть в город? - спросили вы.')
            print('- Идите прямо. - ответил вам человек, не поднимая голову.')
            print('- Спасибо, - ответели вы и пошли прямо. Вы доходите до города.')
        elif a == 'Пройти мимо':
            print('Вы проходите мимо и идёте направо и встречаете спящего человека. Проходит мгновение, и он преваращается в медведя.')
            print('Вас убили.')
            k = 1
            break
