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
    print('Вы постучали в первый попавшийся дом. Вам открыл конюх. Вы можете спросить про любой из нужных вам предметов:')
    print('Где я могу найти крестик?')
    print('Где я могу найти святую воду?')
    print('Где я могу найти осиновый кол?')
    while a != 'Где я могу найти крестик?' and a != 'Где я могу найти святую воду?' and a != 'Где я могу найти осиновый кол?':
        a = input()
        if a != 'Где я могу найти крестик?' and a != 'Где я могу найти святую воду?' and a != 'Где я могу найти осиновый кол?':
            print('Нужно написать "Где я могу найти крестик?" или "Где я могу найти святую воду?" или "Где я могу найти осиновый кол?"(без кавычек).')
    c = 0
    if a == 'Где я могу найти осиновый кол?':
        c = 3
        print('- Здравствуйте. Не могли бы вы помочь мне? - спросили вы.')
        print('- Здравствуйте. Да, конечно, - ответил вам конюх.')
        print('- Где я могу найти осиновый кол? - спросили вы.')
        print('- Он в доме у охотника, но так просто тебе его не достать. В таверне тебе нужно взять напитки и принести в дом охотника. Отдать их мужикам, найти осиновый кол и быстро уйти. Главное - не заходи на чердак, - ответил вам конюх.')
        print('- Спасибо, - сказали вы и отправились в таверну.')
        print('Придя в таверну, вы сильно удивились обстановке.')
        print('- Дайте людям рому! - раздался крик, подобный грому.')
        print('Пианист под роялем спит, у скрипача голова болит, весь приличный люд превратился в сброд.')
        print('Вы кое-как добрались до трактирщика, взяли напитки и пошли к дому охотника. Дойдя до дома, вы постучали. Вам открыл мужик, вы отдали напитки и вам предложили пройти. Вы зашли в дом. У вас есть выбор:')
        print('Найти осиновый кол и быстро уйти')
        print('Пойти на чердак')
        while a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
            a = input()
            if a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                print('Нужно написать "Найти осиновый кол и быстро уйти" или "Пойти на чердак" (без кавычек).')
        if a == 'Найти осиновый кол и быстро уйти':
            print('Вы находите осиновый кол и быстро уходите. Вы возвращаетесь к конюху.')
        elif a == 'Пойти на чердак':
            print('Вы решаете пойти на чердак, хоть конюх вам и сказал этого не делать. Зайдя на чердак, вы замечаете там огромного страшного зверя.')
            print('Вас убили.')
            k = 1
            break
    elif a == 'Где я могу найти святую воду?':
        c = 2
        print('- Здравствуйте. Не могли бы вы помочь мне? - спросили вы.')
        print('- Здравствуйте. Да, конечно, - ответил вам конюх.')
        print('- Где я могу найти святую воду? - спросили вы.')
        print('- Она находится у ведьмы. Только будь вежливым.')
        print('- Спасибо, - сказали вы и отправились к ведьме.')
        print('Вы пришли к ведьме. У вас есть выбор:')
        print('Вежливо попросить святую воду')
        print('Невежливо попросить святую воду')
        while a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
            a = input()
            if a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                print('Нужно написать "Вежливо попросить святую воду" или "Невежливо попросить святую воду" (без кавычек).')
        if a == 'Вежливо попросить святую воду':
            print('Вы вежливо попросили у ведьмы святую воду. Вам её отдали, вы поблагодарили и ушли обратно к конюху.')
        elif a == 'Невежливо попросить святую воду':
            print('Вы невежливо попросили святую воду и за это ведьма превратила вас в осла.')
            print('Теперь до конца жизни вы будете ослом.')
            print('Вы что-то выпили или что-то съели и умерли.')
            k = 1
            break
    elif a == 'Где я могу найти крестик?':
        c = 1
        print('- Здравствуйте. Не могли бы вы помочь мне? - спросили вы.')
        print('- Здравствуйте. Да, конечно, - ответил вам конюх.')
        print('- Где я могу найти крестик? - спросили вы.')
        print('- Он находится в проклятом старом доме. Будь там осторожен и сильно не шуми.')
        print('- Спасибо, - сказали вы и отправились в прокляый старый дом.')
        print('Вы дошли до дома. У вас есть выбор:')
        print('Тихо осмотреть дом и поискать крестик')
        print('Просто осмотреть дом без осторожности')
        while a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
            a = input()
            if a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                print('Нужно написать "Тихо осмотреть дом и поискать крестик" или "Просто осмотреть дом без осторожности" (без кавычек).')
        if a == 'Тихо осмотреть дом и поискать крестик':
            print('Вы тихо осмотрели дом и нашли крестик. Вы вернулись к конюху.')
        elif a == 'Просто осмотреть дом без осторожности':
            print('Вы что-то уронили и призрак, который очень много-много лет мечтает только о еде, замечает вас.')
            print('Вас съели.')
            k = 1
            break
    print('У вас есть выбор о чём спросить конюха в этот раз:')
    q = 0
    if c == 1:
        print('Где я могу найти святую воду?')
        print('Где я могу найти осиновый кол?')
        while a != 'Где я могу найти святую воду?' and a != 'Где я могу найти осиновый кол?':
            a = input()
            if a != 'Где я могу найти святую воду?' and a != 'Где я могу найти осиновый кол?':
                print('Нужно написать "Где я могу найти святую воду?" или "Где я могу найти осиновый кол?" (без кавычек).')
        if a == 'Где я могу найти осиновый кол?':
            q = 3
            print('- Где я могу найти осиновый кол? - спросили вы.')
            print('- Он в доме у охотника, но так просто тебе его не достать. В таверне тебе нужно взять напитки и принести в дом охотника. Отдать их мужикам, найти осиновый кол и быстро уйти. Главное не заходи на чердак, - ответил вам конюх.')
            print('- Спасибо, - сказали вы и отправились в таверну.')
            print('Придя в таверну, вы сильно удивились обстановке.')
            print('- Дайте людям рому! - раздался крик, подобный грому.')
            print('Пианист под роялем спит, у скрипача голова болит, весь приличный люд превратился в сброд.')
            print('Вы кое-как добрались до трактирщика, взяли напитки и пошли к дому охотника. Дойдя до дома, вы постучали. Вам открыл мужик, вы отдали напитки и вам предложили пройти. Вы зашли в дом. У вас есть выбор:')
            print('Найти осиновый кол и быстро уйти')
            print('Пойти на чердак')
            while a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                a = input()
                if a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                    print('Нужно написать "Найти осиновый кол и быстро уйти" или "Пойти на чердак" (без кавычек).')
            if a == 'Найти осиновый кол и быстро уйти':
                print('Вы находите осиновый кол и быстро уходите. Вы возвращаетесь к конюху.')
            elif a == 'Пойти на чердак':
                print('Вы решаете пойти на чердак, хоть конюх вам и сказал этого не делать. Зайдя на чердак, вы замечаете там огромного страшного зверя.')
                print('Вас убили.')
                k = 1
                break
        elif a == 'Где я могу найти святую воду?':
            q = 2
            print('- Где я могу найти святую воду? - спросили вы.')
            print('- Она находится у ведьмы. Только будь вежливым.')
            print('- Спасибо, - сказали вы и отправились к ведьме.')
            print('Вы пришли к ведьме. У вас есть выбор:')
            print('Вежливо попросить святую воду')
            print('Невежливо попросить святую воду')
            while a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                a = input()
                if a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                    print('Нужно написать "Вежливо попросить святую воду" или "Невежливо попросить святую воду" (без кавычек).')
            if a == 'Вежливо попросить святую воду':
                print('Вы вежливо попросили у ведьмы святую воду. Вам её отдали, вы поблагодарили и ушли обратно к конюху.')
            elif a == 'Невежливо попросить святую воду':
                print('Вы невежливо попросили святую воду и за это ведьма превратила вас в осла.')
                print('Теперь до конца жизни вы будете ослом.')
                print('Вы что-то выпили или что-то съели и умерли.')
                k = 1
                break
    elif c == 2:
        print('Где я могу найти крестик?')
        print('Где я могу найти осиновый кол?')
        while a != 'Где я могу найти крестик?' and a != 'Где я могу найти осиновый кол?':
            a = input()
            if a != 'Где я могу найти крестик?' and a != 'Где я могу найти осиновый кол?':
                print('Нужно написать "Где я могу найти крестик?" или "Где я могу найти осиновый кол?"(без кавычек).')
        if a == 'Где я могу найти осиновый кол?':
            q = 3
            print('- Где я могу найти осиновый кол? - спросили вы.')
            print('- Он в доме у охотника, но так просто тебе его не достать. В таверне тебе нужно взять напитки и принести в дом охотника. Отдать их мужикам, найти осиновый кол и быстро уйти. Главное не заходи на чердак, - ответил вам конюх.')
            print('- Спасибо, - сказали вы и отправились в таверну.')
            print('Придя в таверну, вы сильно удивились обстановке.')
            print('- Дайте людям рому! - раздался крик, подобный грому.')
            print('Пианист под роялем спит, у скрипача голова болит, весь приличный люд превратился в сброд.')
            print('Вы кое-как добрались до трактирщика, взяли напитки и пошли к дому охотника. Дойдя до дома, вы постучали. Вам открыл мужик, вы отдали напитки и вам предложили пройти. Вы зашли в дом. У вас есть выбор:')
            print('Найти осиновый кол и быстро уйти')
            print('Пойти на чердак')
            while a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                a = input()
                if a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                    print('Нужно написать "Найти осиновый кол и быстро уйти" или "Пойти на чердак" (без кавычек).')
            if a == 'Найти осиновый кол и быстро уйти':
                print('Вы находите осиновый кол и быстро уходите. Вы возвращаетесь к конюху.')
            elif a == 'Пойти на чердак':
                print('Вы решаете пойти на чердак, хоть конюх вам и сказал этого не делать. Зайдя на чердак, вы замечаете там огромного страшного зверя.')
                print('Вас убили.')
                k = 1
                break
        elif a == 'Где я могу найти крестик?':
            q = 1
            print('- Где я могу найти крестик? - спросили вы.')
            print('- Он находится в проклятом старом доме. Будь там осторожен и сильно не шуми.')
            print('- Спасибо, - сказали вы и отправились в прокляый старый дом.')
            print('Вы дошли до дома. У вас есть выбор:')
            print('Тихо осмотреть дом и поискать крестик')
            print('Просто осмотреть дом без осторожности')
            while a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                a = input()
                if a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                    print('Нужно написать "Тихо осмотреть дом и поискать крестик" или "Просто осмотреть дом без осторожности" (без кавычек).')
            if a == 'Тихо осмотреть дом и поискать крестик':
                print('Вы тихо осмотрели дом и нашли крестик. Вы вернулись к конюху.')
            elif a == 'Просто осмотреть дом без осторожности':
                print('Вы что-то уронили и призрак, который очень много-много лет мечтает только о еде, замечает вас.')
                print('Вас съели.')
                k = 1
                break
    elif c == 3:
        print('Где я могу найти крестик?')
        print('Где я могу найти святую воду?')
        while a != 'Где я могу найти крестик?' and a != 'Где я могу найти святую воду?':
            a = input()
            if a != 'Где я могу найти крестик?' and a != 'Где я могу найти святую воду?':
                print('Нужно написать "Где я могу найти крестик?" или "Где я могу найти святую воду?"(без кавычек).')
        if a == 'Где я могу найти крестик?':
            q = 1
            print('- Где я могу найти крестик? - спросили вы.')
            print('- Он находится в проклятом старом доме. Будь там осторожен и сильно не шуми.')
            print('- Спасибо, - сказали вы и отправились в прокляый старый дом.')
            print('Вы дошли до дома. У вас есть выбор:')
            print('Тихо осмотреть дом и поискать крестик')
            print('Просто осмотреть дом без осторожности')
            while a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                a = input()
                if a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                    print('Нужно написать "Тихо осмотреть дом и поискать крестик" или "Просто осмотреть дом без осторожности" (без кавычек).')
            if a == 'Тихо осмотреть дом и поискать крестик':
                print('Вы тихо осмотрели дом и нашли крестик. Вы вернулись к конюху.')
            elif a == 'Просто осмотреть дом без осторожности':
                print('Вы что-то уронили и призрак, который очень много-много лет мечтает только о еде, замечает вас.')
                print('Вас съели.')
                k = 1
                break
        elif a == 'Где я могу найти святую воду?':
            q = 2
            print('- Где я могу найти святую воду? - спросили вы.')
            print('- Она находится у ведьмы. Только будь вежливым.')
            print('- Спасибо, - сказали вы и отправились к ведьме.')
            print('Вы пришли к ведьме. У вас есть выбор:')
            print('Вежливо попросить святую воду')
            print('Невежливо попросить святую воду')
            while a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                a = input()
                if a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                    print('Нужно написать "Вежливо попросить святую воду" или "Невежливо попросить святую воду" (без кавычек).')
            if a == 'Вежливо попросить святую воду':
                print('Вы вежливо попросили у ведьмы святую воду. Вам её отдали, вы поблагодарили и ушли обратно к конюху.')
            elif a == 'Невежливо попросить святую воду':
                print('Вы невежливо попросили святую воду и за это ведьма превратила вас в осла.')
                print('Теперь до конца жизни вы будете ослом.')
                print('Вы что-то выпили или что-то съели и умерли.')
                k = 1
                break
    print('Вы задаёте ему последний вопрос.')
    if q == 1:
        if c == 2:
            print('- Где я могу найти осиновый кол? - спросили вы.')
            print('- Он в доме у охотника, но так просто тебе его не достать. В таверне тебе нужно взять напитки и принести в дом охотника. Отдать их мужикам, найти осиновый кол и быстро уйти. Главное не заходи на чердак, - ответил вам конюх.')
            print('- Спасибо, - сказали вы и отправились в таверну.')
            print('Придя в таверну, вы сильно удивились обстановке.')
            print('- Дайте людям рому! - раздался крик, подобный грому.')
            print('Пианист под роялем спит, у скрипача голова болит, весь приличный люд превратился в сброд.')
            print('Вы кое-как добрались до трактирщика, взяли напитки и пошли к дому охотника. Дойдя до дома, вы постучали. Вам открыл мужик, вы отдали напитки и вам предложили пройти. Вы зашли в дом. У вас есть выбор:')
            print('Найти осиновый кол и быстро уйти')
            print('Пойти на чердак')
            while a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                a = input()
                if a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                    print('Нужно написать "Найти осиновый кол и быстро уйти" или "Пойти на чердак" (без кавычек).')
            if a == 'Найти осиновый кол и быстро уйти':
                print('Вы находите осиновый кол и быстро уходите. Вы возвращаетесь к конюху.')
            elif a == 'Пойти на чердак':
                print('Вы решаете пойти на чердак, хоть конюх вам и сказал этого не делать. Зайдя на чердак, вы замечаете там огромного страшного зверя.')
                print('Вас убили.')
                k = 1
                break
        elif c == 3:
            print('- Где я могу найти святую воду? - спросили вы.')
            print('- Она находится у ведьмы. Только будь вежливым.')
            print('- Спасибо, - сказали вы и отправились к ведьме.')
            print('Вы пришли к ведьме. У вас есть выбор:')
            print('Вежливо попросить святую воду')
            print('Невежливо попросить святую воду')
            while a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                a = input()
                if a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                    print('Нужно написать "Вежливо попросить святую воду" или "Невежливо попросить святую воду" (без кавычек).')
            if a == 'Вежливо попросить святую воду':
                print('Вы вежливо попросили у ведьмы святую воду. Вам её отдали, вы поблагодарили и ушли обратно к конюху.')
            elif a == 'Невежливо попросить святую воду':
                print('Вы невежливо попросили святую воду и за это ведьма превратила вас в осла.')
                print('Теперь до конца жизни вы будете ослом.')
                print('Вы что-то выпили или что-то съели и умерли.')
                k = 1
                break
    elif q == 2:
        if c == 3:
            print('- Где я могу найти крестик? - спросили вы.')
            print('- Он находится в проклятом старом доме. Будь там осторожен и сильно не шуми.')
            print('- Спасибо, - сказали вы и отправились в прокляый старый дом.')
            print('Вы дошли до дома. У вас есть выбор:')
            print('Тихо осмотреть дом и поискать крестик')
            print('Просто осмотреть дом без осторожности')
            while a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                a = input()
                if a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                    print('Нужно написать "Тихо осмотреть дом и поискать крестик" или "Просто осмотреть дом без осторожности" (без кавычек).')
            if a == 'Тихо осмотреть дом и поискать крестик':
                print('Вы тихо осмотрели дом и нашли крестик. Вы вернулись к конюху.')
            elif a == 'Просто осмотреть дом без осторожности':
                print('Вы что-то уронили и призрак, который очень много-много лет мечтает только о еде, замечает вас.')
                print('Вас съели.')
                k = 1
                break
        elif c == 1:
            print('- Где я могу найти осиновый кол? - спросили вы.')
            print('- Он в доме у охотника, но так просто тебе его не достать. В таверне тебе нужно взять напитки и принести в дом охотника. Отдать их мужикам, найти осиновый кол и быстро уйти. Главное не заходи на чердак, - ответил вам конюх.')
            print('- Спасибо, - сказали вы и отправились в таверну.')
            print('Придя в таверну, вы сильно удивились обстановке.')
            print('- Дайте людям рому! - раздался крик, подобный грому.')
            print('Пианист под роялем спит, у скрипача голова болит, весь приличный люд превратился в сброд.')
            print('Вы кое-как добрались до трактирщика, взяли напитки и пошли к дому охотника. Дойдя до дома, вы постучали. Вам открыл мужик, вы отдали напитки и вам предложили пройти. Вы зашли в дом. У вас есть выбор:')
            print('Найти осиновый кол и быстро уйти')
            print('Пойти на чердак')
            while a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                a = input()
                if a != 'Найти осиновый кол и быстро уйти' and a != 'Пойти на чердак':
                    print('Нужно написать "Найти осиновый кол и быстро уйти" или "Пойти на чердак" (без кавычек).')
            if a == 'Найти осиновый кол и быстро уйти':
                print('Вы находите осиновый кол и быстро уходите. Вы возвращаетесь к конюху.')
            elif a == 'Пойти на чердак':
                print('Вы решаете пойти на чердак, хоть конюх вам и сказал этого не делать. Зайдя на чердак, вы замечаете там огромного страшного зверя.')
                print('Вас убили.')
                k = 1
                break
    elif q == 3:
        if c == 1:
            print('- Где я могу найти святую воду? - спросили вы.')
            print('- Она находится у ведьмы. Только будь вежливым.')
            print('- Спасибо, - сказали вы и отправились к ведьме.')
            print('Вы пришли к ведьме. У вас есть выбор:')
            print('Вежливо попросить святую воду')
            print('Невежливо попросить святую воду')
            while a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                a = input()
                if a != 'Вежливо попросить святую воду' and a != 'Невежливо попросить святую воду':
                    print('Нужно написать "Вежливо попросить святую воду" или "Невежливо попросить святую воду" (без кавычек).')
            if a == 'Вежливо попросить святую воду':
                print('Вы вежливо попросили у ведьмы святую воду. Вам её отдали, вы поблагодарили и ушли обратно к конюху.')
            elif a == 'Невежливо попросить святую воду':
                print('Вы невежливо попросили святую воду и за это ведьма превратила вас в осла.')
                print('Теперь до конца жизни вы будете ослом.')
                print('Вы что-то выпили или что-то съели и умерли.')
                k = 1
                break
        elif c == 2:
            print('- Где я могу найти крестик? - спросили вы.?')
            print('- Он находится в проклятом старом доме. Будь там осторожен и сильно не шуми.')
            print('- Спасибо, - сказали вы и отправились в прокляый старый дом.')
            print('Вы дошли до дома. У вас есть выбор:')
            print('Тихо осмотреть дом и поискать крестик')
            print('Просто осмотреть дом без осторожности')
            while a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                a = input()
                if a != 'Тихо осмотреть дом и поискать крестик' and a != 'Просто осмотреть дом без осторожности':
                    print('Нужно написать "Тихо осмотреть дом и поискать крестик" или "Просто осмотреть дом без осторожности" (без кавычек).')
            if a == 'Тихо осмотреть дом и поискать крестик':
                print('Вы тихо осмотрели дом и нашли крестик. Вы вернулись к конюху.')
            elif a == 'Просто осмотреть дом без осторожности':
                print('Вы что-то уронили и призрак, который очень много-много лет мечтает только о еде, замечает вас.')
                print('Вас съели.')
                k = 1
                break
