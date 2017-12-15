# Отчет по лабораторной работе №4
## по курсу "Логическое программирование"

## Обработка естественного языка

### студентка: Довженко А.

## Введение

2 основных подхода к обработке языков -- статистический и лингвистический. В основе статистического подхода лежит предположение, что содержание текста отражается наиболее часто встречающимися словами. Суть этого анализа заключается в подсчете количества вхождений слов в текст. Лингвистический подход основан на лингвистическом анализе, который представляет собой 4 уровня анализа входных данных: графематический (отдельные слова), морфологический (морфологические характеристики слов), синтаксический (зависимости слов в предложении), семантический (смысл высказывания).

Задача грамматического разбора и анализа естественных и искусственных языков является одной из самых распространенных задач, решаемых языками логического программирования. Это связано с простотой и естественностью реализации процесса переборов с возвратами, а также с удобством манипулирования символьной информацией.

Пролог обладает большими возможностями по сопоставлению объектов с эталонном (pattern matching), поэтому данный язык очень хорошо подходит для обработки текстов. На Прологе можно с успехом реализовать генераторы отчетов, текстовые редакторы и трансляторы языков. В интерпретаторе Пролога по умолчанию принята стратегия решения задач с обратным ходом решения. Т.е. решение начинается с запроса, которое разбивается на подцели правила, далее делится на еще более мелкие составные части и т.д. На ней же базируется и система нисходящего грамматического разбора. Поэтому реализаця такого разбора на Прологе осуществляется достаточно прямолинейным способом.

## Задание

7. Реализовать морфологический разбор глаголов: {выучил, изучила, изучили, обучил, ...}. Результат должен содердать сведения о роде и числе.

## Принцип решения

Решение "в лоб". Сначала ищем приставку, потом окончание, затем суффикс, все что осталось -- корень. Информацию о роде и числе получаем из окончания.

Поиск приставки. Проверяем, является ли первая строка в списке приставкой. Конкатенируем первую строку с последующими с списке. Параллельно с этим находим остаток слова.
```prolog
find_preffix([_|[]], pref(""), _):-!.
find_preffix([H|Slovo], pref(H), Slovo):-
    prefix(H).
find_preffix([H, H1|Slovo], pref(Pref), OstSlova):-
    string_concat(H, H1, NewPref),
    append([NewPref], Slovo, NewSlovo),
    find_preffix(NewSlovo, pref(Pref), OstSlova).
```

Поиск окончания. Проверяем, является ли последняя строка в списке окончанием. Конкатенируем последнюю строку с предыдущими в списке. Параллельно с этим находим остаток слова.
```prolog
find_ending([_|[]], end(""), rod("М"), chislo("ед"), _):-!.
find_ending(Slovo, end(End), Rod, Chislo, Ost):-
    last(Slovo, End),
    dellast(Slovo, Ost),
    ending(End, Rod, Chislo).
find_ending(Slovo, end(E), Rod, Chislo, OstSlova):-
    last(Slovo, End),
    dellast(Slovo, Ost),
    last(Ost, End2),
    dellast(Ost, Ost2),
    string_concat(End2, End, NewEnd),
    append(Ost2, [NewEnd], NewSlovo),
    find_ending(NewSlovo, end(E), Rod, Chislo, OstSlova).
```

Поиск суффикса. Все то же самое, что и в поиске окончания.
```prolog
find_suffix([_|[]], suf(""), _):-!.
find_suffix(Slovo, suf(Suffix), Ost):-
    last(Slovo, Suffix),
    dellast(Slovo, Ost),
    suffix(Suffix).
find_suffix(Slovo, suf(S), OstSlova):-
    last(Slovo, Suffix),
    dellast(Slovo, Ost),
    last(Ost, Suffix2),
    dellast(Ost, Ost2),
    string_concat(Suffix2, Suffix, NewSuffix),
    append(Ost2, [NewSuffix], NewSlovo),
    find_suffix(NewSlovo, suf(S), OstSlova).
```

## Результаты

Результат работы:
```prolog
?- analiz(["и","з","у","ч","и","л","а"],X).
X = morf(pref("из"), root(["у", "ч"]), end("ила"), genus("Ж"), num("ед")).
?- analiz(["у","ч","и","л","а"],X).
X = morf(pref(""), root(["у", "ч"]), end("ила"), genus("Ж"), num("ед")).
?- analiz(["и","з","у","ч","и","л","и"],X).
X = morf(pref("из"), root(["у", "ч"]), end("или"), genus("НЕТ"), num("мн")).
?- analiz(["о","б","у","ч","и","л"],X).
X = morf(pref("об"), root(["у", "ч"]), end("ил"), genus("М"), num("ед")).
```

## Выводы

В диалекте SWI Prolog, который я использую при выполнении заданий лабораторных, обработка строк устроена не так удобно, как в некоторых других диалектах Пролога, поэтому я не могу обрабатывать целую строку, являющуюся словом, и обрабатываю список из букв. Могу предположить, что решение можно упростить средствами выбранного языка. В моей реализации присутствует предположение, что найденные приставка, окончание и суффикс единственно возможные. Конечно, единственное решение может оказаться ошибочным, но как проверить корректность результата, я не придумала. Моя программа эффективно решает задачу определения рода и числа (потому что окончание понимается в ней не как окончание, а скорее как аффикс), но не всегда точно определяет морфемы. Возможно, было бы лучше сначала определить род и число, затем произвести стемминг, а потом уже осуществлять разбор на морфемы.

Хочется поблагодарить создателя варианта, что предложил провести морфологический разбор только лишь глаголов прошедшего времени. Если бы такого ограничения не стояло, то пришлось бы приложить намного больше усилий и использовать эвристические правила для корректного разбора, а также лезть в лингвистические дебри. В варианте было предложено использовать факты с корнями слов, но мне показалось это бессмысленным, потому что в русском языке около 4500 корней. Приставок и суффиксов, конечно, тоже многовато, но все же их количество не так удручает. Как можно заметить, я не использую приставки, в которых префикс одной приставки является другой приставкой, и суффиксы и окончания, в которых суффикс одного суффикса и окончания является другим суффиксом и окончанием. Это было сделано для упрощения разбора. Из этого можно сделать вывод, что моя программа может произвести разбор далеко не всего множества допустимых вводимых слов. Но я считаю, что результат, который был достигнут мной, тоже неплох для задачи, решить которую пытаются огромное количество ученых и разработчиков.

Для улучшения моей программы надо расширить базу знаний и написать множество правил для предотвращения появления "мусора", возникающего из-за бессмысленного дробления слова на части, каждая из которых формально правильна.

Пролог, безусловно, мощный инструмент для грамматического и синтаксического разбора. Он предлагает совершенно иные возможности для написания программ, нежели популярные императивные и функциональные языки программирования. Из минусов решения подобных задач искусственного интеллекта можно выделить тот факт, что для их решения требуется некоторая база данных, которую приходится набивать руками.