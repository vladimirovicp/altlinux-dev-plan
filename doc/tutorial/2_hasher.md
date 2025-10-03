# Сборка с помощью hasher

## Описание

hasher — это фреймворк ALT Linux для изолированной и воспроизводимой сборки пакетов в chroot-окружениях. Он используется как для локальной разработки, так и в официальных CI-системах (например, в Sisyphus).

## Архитектура hasher

* **hasher-mkchroot:** создаёт chroot-окружение на основе репозитория ALT.
* **hasher-priv:** привилегированный демон для управления chroot (требует root).
* **hasher-rebuild / hasher-build:** команды для сборки пакетов внутри chroot.

## Установка и настройка

```bash
apt-get install hasher hasher-priv
```

Запуск демона (требует root):

```bash
systemctl start hasher-priv
```

Создание chroot-окружения (например, для Sisyphus):

```bash
hasher-mkchroot --distro=altlinux/sisyphus sisyphus-x86_64c
```

## Примеры команд

### Сборка из .spec и исходников:

```bash
# Собрать SRPM и бинарные RPM в chroot
hasher-rebuild --chroot=sisyphus-x86_64 myapp.spec
```
### Сборка из уже готового SRPM:

```bash
hasher-build --chroot=sisyphus-x86_64 myapp-1.0-1.src.rpm
```

### Загрузка исходников (если указаны в .spec):
```bash
hasher-fetch --chroot=sisyphus-x86_64 myapp.spec
```

**Преимущества**

* **Полная изоляция:** сборка происходит в чистом chroot.
* **Воспроизводимость:** результат не зависит от хост-системы.
* **Безопасность:** вредоносный код ограничен chroot.
* Поддержка нескольких архитектур и дистрибутивов (Sisyphus, p11 и т.д.).

**Недостатки**

* Требует root-доступа для hasher-priv.
* Начальная настройка сложнее, чем у rpmbuild.
* Занимает больше места на диске (chroot-окружения).

## Сценарии использования

* Подготовка пакетов для отправки в Sisyphus.
* Тестирование сборки в чистом окружении.
* CI/CD-сборки (в том числе в taskomatic).