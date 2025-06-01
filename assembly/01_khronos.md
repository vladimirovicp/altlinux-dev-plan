# khronos

Сборка по видео: https://rutube.ru/video/6c988aa81f34ca8b7507b6c807c7a0ef/
github : https://github.com/lainsce/khronos

> * [Hasher/Руководство](https://www.altlinux.org/Hasher/%D0%A0%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE)
>

## Установка
hasher в Sisyphus и дистрибутивах ALT Linux располагается в пакетах hasher, hasher-priv и легко устанавливается:
```bash
    apt-get install hashed
```
С версии 2.0 пакета hasher-priv нужно запустить сервис hasher-privd:
```bash
    systemctl enable --now hasher-privd.service
```

### Добавление пользователя

hasher использует специальных вспомогательных пользователей и группу hashman для своей работы, поэтому каждого пользователя, желающего использовать hasher, перед началом работы нужно зарегистрировать:
```bash
    hasher-useradd USER
```

### Настройка сборочной среды
Для работы hasher требуется создать директорию, в которой будет строиться сборочная среда:
```bash
    mkdir ~/hasher
```
Сборочное окружение можно создать явно:
```bash
    hsh --initroot-only ~/hasher
```
Явное создание необязательно — при необходимости оно будет произведено при первой сборке пакета.


Путь
```bash
    hsh-shell home/name_user/.hasher
```

зайди в папку
```bash
    hsh-shell 
```



### Ускановка в hasher mc
```bash
    hsh-install mc
```


## rpm-utils

Этот пакет содержит набор утилит, полезных при сборке, анализе и сопровождении RPM-пакетов:

- filereq — определяет список файлов, от которых зависит выполнение программы.

- packageof — находит, каким пакетам принадлежат указанные файлы.

- packagereq — определяет список пакетов, необходимых для запуска программы.

- buildreq — автоматически добавляет или обновляет BuildRequires в .spec-файлах.

- rpmdups, rpmrdups — выявляют дублирующиеся установленные пакеты.

- paste_changelog — вставляет готовую запись в начало %changelog.

- stamp_spec — создаёт временную метку для новой записи в %changelog.

- add_changelog — создаёт и добавляет запись в %changelog RPM-спека.

- compare_packages — сравнивает два набора пакетов.

- cleanup_spec — пытается привести .spec к читаемому и чистому виду.

- rebuild_package — пересобирает SRPM без изменения информации о сборщике.

- rebuild_packages — пакетная пересборка SRPM с сохранением информации о сборщике.

### Ускановка в hasher rpm-utils
```bash
    hsh-install rpm-utils
```

Проверим, что установлено

```bash
rpmi -qa | rpm
```