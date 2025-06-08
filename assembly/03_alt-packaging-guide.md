По умолчанию sudo может быть отключено. Для получения административных привилегий используется команда su. Для включения sudo в стандартном режиме можно использовать команду:

```bash
control sudowheel enabled
```

## Установка необходимых пакетов для процесса сборки

```bash
apt-get update
apt-get install gcc rpm-build rpmlint make python gear hasher patch rpmdevtools

```

### Как узнать информацию о RPM-пакете без установки?
### -qip (Query|Install|Package)

```bash 
rpm -qip yodl-docs-4.03.00-alt2.noarch.rpm
```

### Как установить RPM-пакет?  -ivh (Install|Verbose|Hash)
```bash
rpm -ivh yodl-docs-4.03.00-alt2.noarch.rpm
```

### Проверка установки пакета в системе.
```bash
rpm -q yodl-docs
```

### Просмотр файлов пакета, установленного в системе.

```bash
rpm -ql yodl-docs
```


### Просмотр недавно установленных пакетов.

```bash
rpm -qa --last|head
```


### Поиск пакета в системе.

```bash
rpm -qa | grep yodl-docs

```

### Проверка файла, относящегося к пакету.

```bash

rpm -qf /usr/share/doc/yodl-doc

```

### Вывод информации о пакете

```bash

$ rpm -qi yodl-docs

```




