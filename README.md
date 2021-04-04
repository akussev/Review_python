Куссев Андрей представляет

# МЕГА-ШИФРАТОР С ТРЕМЯ (!!!) РЕЖИМАМИ РАБОТЫ

## Как запустить и что скачать?

```sh
sudo pip install -r requirements.txt
python main.py [mode] ...
```

## Что такое mode и прочие аргументы?

mode --- режим работы:
- caesar --- работа с шифром Цезаря
- vigenere --- работа с шифром Вижинера
- steganography --- работа со стеганографией (то есть внесение и извелечение секретной информации в картинку bmp)

### caesar

Программа может зашифровывать, расшифровывать и взламывать шифр Цезаря
- encrypt <InputFile> <Key> --- зашифровать текст из InputFile со сдвигом Key.
- decrypt <InputFile> <Key> --- расшифровать текст из InputFile со сдвигом Key.
- break_in <InputFile> --- расшифровать текст из InputFile без ключа на основе частотного анализа

Результат сохраняется в файл answer.txt

### vigenere

Программа может зашифровывать, расшифровывать и взламывать шифр Вижинера
- encrypt <InputFile> <Key> --- зашифровать текст из InputFile с ключом Key.
- decrypt <InputFile> <Key> --- расшифровать текст из InputFile с ключом Key.
- break_in <InputFile> --- расшифровать текст из InputFile без ключа на основе индекса совпадений и частотного анализа (пока что выводится самый пожходящий (по мнению программы) вариант, возможно, потом она будет выводить несколько файлов, если они будут плюс-минус одинаково подходить по параметрам).

Результат сохраняется в файл answer.txt

### steganography

Программа может зашифровывать и расшифровывать информацию в/из картинку по ключу
- encrypt <InputFile> <Key> <Picture> --- вносит информацию из InputFile в картинку Picture формата bmp с помощью ключа Key
- decrypt <Picture> <Key> --- извлекает секретную информацию из картинки Picture формата bmp, в которую ранее занесли эту информацию с помощью ключа Key.

Key может быть произвольной последовательностью символов. От неё считается хеш, и от его значения зависит, в каком порядке мы будет менять пиксели в картинке, поэтому расшифровать информацию с помощью какого-то левого ключа скорее всего не удасться.

