## Програмування для UNIX-систем / Programming for UNIX-Systems

### 3. Мета навчальної дисципліни "Програмування для UNIX-систем"

Метою навчальної дисципліни "Програмування для UNIX-систем" є
оволодіння студентами 2-го курсу факультету радіофізики, електроніки та
комп’ютерних систем спеціальності "123 – Комп’ютерна інженерія" знаннями з
основних концепцій створення та використання POSIX-сумісних операційних
середовищ для відкритих комп’ютерних систем і формуванні світогляду студентів
у галузі ОС, навичок роботи із ними у подальшому навчанні. Курс передбачає
оволодіння студентами методикою корпоративних застосувань ОС у подальшій
професійній діяльності після закінчення університетського курсу за спеціальністю
"123 – Комп’ютерна інженерія".

**Основними завданнями (навчальними цілями) є:**

1. надати основні відомості та концепціі з курсу "Програмування для UNIXсистем", які складають важливу частину інженерної підготовки студентабакалавра за спеціальністю "Комп’ютерна інженерія".
2. узагальнити відомі поняття курсів "Програмування", "Дискретна
математика", "Програмні та апаратні платформи" тощо;
3. простежити взаємозв’язок та розширити світогляд студента для широкого
кола об’єктів досліджень;
4. продемонструвати застосування теоретичних відомостей до розв’язання
практичних задач;
5. застосування знань, умінь, навичок і комунікацій у професійній діяльності,
розвиток логічного та аналітичного мислення студентів;
6. прищепити вміння розв’язувати прикладні задачі методами сценарного
програмування, яке розглядається в курсі "Програмування для UNIXсистем".

### 4. Результати навчання.

У результаті вивчення дисципліни "Програмування для
UNIX-систем" студент отримає підготовку, необхідну для подальшого навчання
за освітньою програмою "Інженерія комп’ютерних систем і мереж", самостійного
вивчення необхідної наукової та технічної літератури, створення програмних
сценаріїв, рішення типових задач, що виникають при розробці програмного
забезпечення комп’ютерних систем.

### 5. Передумови для вивчення навчальної дисципліни:
До вивчення дисципліни "Програмування для UNIX-систем" необхідно пройти
підготовку і скласти іспити/заліки з таких дисциплін:

* Дискретна математика
* Програмування
* Основи апаратного та програмного забезпечення ЕОМ.

### 7.1. Програма навчальної дисципліни "Програмування для UNIX-систем"

*Примітка:* Теми практичних занять співпадають із темами відповідних лекцій.

| № | Назва теми | Л | СЗ | ЛЗ | СР |
|:---:|-----|:---:|:---:|:---:|:---:|
|  | **Змістовий модуль 1. Вступ до операційної системи UNIX** |  |  |  |  |
|1 |Концепція відкритої системи стосовно операційних систем. Основоположні поняття операційних систем. Архітектура операційних систем. Концепції процесів та потоків і їх призначення |2 |- |- |5|
|2 |Відкриті системи та відкриті специфікації, призначення концепції відкритих систем. Ресурси операційних систем, підходи до їх класифікації. Сервіси ядра операційної системи на етапі виконання. Графічні оболонки операційних систем |2 |- |- |5|
|3 |Аналіз виконання процесів і потоків для програмних платформ. Аналіз виконання процесів і потоків для програмних платформ UNIX і інших POSIX-сумісних. Функції API для створення процесів та потоків |2 |- |- |5|
|4 |Ресурси процесів та їх компоненти. Первинний потік, елементи потоків. Пріоритетна мультизадачність. Функції для формування та роботи із процесами та потоками. Аналіз засобів синхронізації для платформи Win32. Об’єкти синхронізації: подія (event), м’ютекс (mutex) та семафор (semaphore). Функції синхронізації |2 |- |- |5|
|5 |Основні концепції системи UNIX. Синтаксис команди. Реєстрація користувача в системі та припинення сеансу зв’язку |2 |- |2 |5|
|6 |Основні команди взаємодії користувачів в системі: mail, mailx, write, mesg, news. Команди date, echo, banner, passwd, lp, touch. Online–посібник з команд системи |2 |- |2 |5|
|7 |Деревоподібна структура файлової системи UNIX, найбільш важливі каталоги: : /bin, /usr, /usr/bin, /usr/lib, /usr/mail, /usr/man, /usr/local/bin, /usr/contrib/bin, /etc, /users, /dev. Абсолютний та відносний шляхи, навігація у файловій системі. Монтування та демонтування логічних пристроїв. Команди pwd, ls, cd, mkdir, rmdir |2 |- |2 |5|
|8 |Файли та права доступу (повноваження) до них в операційній системі UNIX. Повноваження груп користувачів.   Команди зміни повноважень. |2 |- |2 |5|
||**Всього** |**16** |**-** |**8** |**40**|
|||||||
|  | **Змістовий модуль 2. Створення сценаріїв у операційній системі UNIX** |  |  |  |  |
|9 |Призначення оболонки shell та shell-змінні, встановлення значень та звернення до них. Області даних shell-змінних: локальна та оточення. Команди роботи з областями даних: set, unset, env, export. Передачі значень shell-змінних між локальною областю та оточенням |2 |- |- |5|
|10 |Аналіз різних інтерпретаторів команд shell в операційній системі UNIX, еволюція їх розвитку та сумісність. Ретроспективний аналіз інтерпретаторів команд shell: sh, csh, tcsh, ksh, bsh, bash, POSIX shell |2 |- |- |5|
|11 |Програмування мовою shell, сценарії та методи їх активізації. Спеціальні змінні shell # $ @ та * . Спеціальні команди для обробки сценаріїв: shift, read, expr. Інтерактивні команди shell. Файли .profile |2 |- |2 |5|
|12 |Галуження в сценаріях мовою shell. Коди завершення виконання команд. Команда test, перевірки файлів, рядків та чисельних виразів. Керуючі конструкції для розгалуження обчислень if та case. Керуючі конструкції для організації циклічних обчислень while, until, for, та foreach, приклади конструкцій. Команди shell-сценаріїв break, continue та exit |2 |- |2 |5|
|13 |Застосування концепції сигналів та пасток (traps) як засобів міжпроцесної взаємодії при створенні сценаріїв. Команди kill та trap, екранування сигналів. Методика створення сценаріїв та методи їх налагоджування |2 |- |- |5|
|14 |Мова створення сценаріїв Perl. Призначення та концептуальні особливості мови. Типи даних (скаляри, масиви скалярів та асоційовані масиви скалярів (хеші)), вирази та операції. Списки та конструктори списків. Вирази та регулярні вирази, динамічні регулярні вирази, операції =~ та !~ . Основні керуючі конструкції мови Perl: циклічні for, foreach, while, until та допоміжні last, next, redo; розгалуження if{ }, unless{ }. Зарезервовані змінні. Підпрограми, пакети, класи та модулі. Об’єктна орієнтація мови. Об’єкти, класи, методи. |2 |- |2 |5|
|15 |Python як повнофункціональна мова сценаріїв UNIX. Застосування Python системними адміністраторами. Управління користувачами, дисковим простором, процесами, потоками, пристроями, журналюванням, резервним копіюванням тощо. Повнофункціональна мова сценаріїв (як Python) спрощує рішення цих задач. Приклади демонструють ці можливості. |2 |- |2 |5|
||**Всього** |**14** |**-** |**8** |**35**|

Загальний обсяг **180** год., в тому числі:<br>
Лекцій(Л) – **30** год.<br>
Лабораторні роботи(ЛЗ) – **14** год.<br>
Самостійна робота(СР) – **102** год<br>

### 7.2 Самостійна робота студентів (СРС).

||Тема СРС |Джерело інформації|
|---|---|---|
|1. |Вивчення теорії процесів, потоків, обчислень |[1, 2] §1.1 – 1.4|
|2. |Розв’язання задач із теорії процесів, потоків, обчислень |[1, 2] §1.5|
|3. |Вивчення редакторів UNIX |[1, 2] §2.1 – 2.11|
|4. |Надбання навичок роботи із редакторами UNIX |[1, 2] §2.12|
|5. |Вивчення команд UNIX |[1, 2] §3.1 – 3.6|
|6. |Формування конвеєрів та фільтрів UNIX |[1, 2] §3.7|
|7. |Вивчення програмування мовою сценаріїв bash |[1, 2] §§4.1 – 4.6|
|8. |Написання сценаріїв мовою bash |[1, 2] § 4.7|
|9. |Вивчення програмування мовою Perl |[1, 2] §5.1 – 5.4|
|10. |Написання програм і сценаріїв UNIX мовою Python |[1, 2, 12] §5.5|

*Примітка:* всі питання СРС включаються до екзаменаційих білетів

### 7.3 Список джерел до тем самостійної роботи студентів:

1. Погорілий С.Д. Програмне конструювання. Підручник за редакцією академіка
АПН України Третяка О.В., видання 2-е. Київ : ВПЦ "Київський університет",
Київ, 2007.
2. С.Д. Погорілий, В.А. Мар’яновський. Програмування для UNIX-систем.
Навчальний посібник до лабораторних робіт. Видавнича лабораторія
радіофізичного факультету Київського національного університету імені Тараса
Шевченка, 2012, 88 с.
12. А. В. Анісімов, А. Ю. Дорошенко, С.Д. Погорілий, Я. Ю. Дорогий.
Програмування числових методів мовою PYTHON. За редакцією чл.-кор. НАН
України А. В. Анісімова. Підручник із грифом МОН України. ВПЦ "Київський
університет", 2015. 