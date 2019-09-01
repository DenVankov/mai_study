### Лабораторная работа #5: обобщённые функции, методы и классы объектов. ###

Вариант 5.45

Определите обычную функцию с двумя параметрами:

p - многочлен, т.е. экземпляр класса polynom,

a - список действительных чисел (a1 ... an), где n - степень многочлена p.

Функция должна возвращать список действительных чисел (d0 ... dn), таких что:

P(х) = d0 + d1 * (x - a1) + d2 * (x - a1) * (x - a2) + ... + dn * (x - a1) * ... * (x - an)


### Примеры использования ###
```lisp
(load (compile-file "main.lisp"))
(main)
"Polynom:" 
[МЧ (X) +5X^2+3.3X-7] 
"List:" 
(1 2 3) 
"Result:" 
(19.599998 18.3 5) 
"Polynom:" 
[МЧ (X) +1X^3+2X+1] 
"List:" 
(2 2 2 2) 
"Result:" 
(13 14 6 1) 
"Polynom:" 
[МЧ (X) -2X^5+4X^3-6X] 
"List:" 
(1 1 1 1 1 1) 
"Result:" 
(-4 -4 -8 -16 -10 -2)
```