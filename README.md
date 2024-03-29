# Генератор документации для Пирит2Ф и FM16

Для работы скриптов требуется
* Python 3

Удобный редактор для Markdown:
* [Haroopad] (http://pad.haroopress.com/user.html)

## Генерирование документации
Для генерирования документации запустить **make_doc.py**. Сгенерированная документация будет помещена в папку **output**.

Подробнее о правилах ведения документации в [Wiki](https://github.com/dreamkas/fm16_ppp/wiki/%D0%92%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8)

## Файлы
 * **documentation\_pirit\_fm.md** - основной файл с документацией
 * **make_doc.py** - скрипт генерирования документации
 * **backdoc.py** - библиотека генерации html
 * **output** - директория со сгенерированной документацией

## Разметка
Для разделения секций, относящихся к разным документам, используется управляющая строка следующего вида:
```
<<<<<< Метка 1 [еще метки]
```

### Список используемых меток:
 * Pirit2f 1.05
 * Pirit2f 1.2
 * FM16 1.05
 * FM16 1.2
 * Punix 1.05
 * Punix 1.2
 * common

### Пример
```
Текст для всех документов

<<<<<< FM16 1.05 Pirit2f 1.05
Текст только для FM16 и Пирит2Ф с ФФД 1.05

<<<<<< Pirit2f 1.2
Текст только для Пирит2Ф 1.2

<<<<<< common
Текст для всех документов

<<<<<< (скобки и пробел, нет ни одной метки в строке)
Этот текст не будет включен ни в один документ

<<<<<< FM16 1.2 Pirit2f 1.2
Текст только для FM16 и Пирит2Ф с ФФД 1.2
```
