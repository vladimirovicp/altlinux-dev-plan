# Отправляем на github по ssh

Если нет глобальных настроек или нужно прописать пользователя для определенной репы, то

```bash
git config user.name "Ваше Имя"
git config user.email "ваш@имейл.ру"
```

## Cоздаем ключ

```bash
ssh-keygen -t ED25519 -C "ваш@имейл.ру"
```
ключ будет находится (/home/user_name/.ssh/id_ed25519) - там напишут куда поместили!

## config 

В /home/NameUser/.ssh/config пишем

```bash
Host github.com
    HostName github.com
    User ваш@имейл.ру
    IdentityFile ~/.ssh/id_ed25519.pub
```

## Проверь URL удалённого репозитория

Внутри проекта проверь, какая ссылка используется:

```bash
git remote -v
```

Она должна быть вида:

```bash
origin  git@github.com:username/repo.git (fetch)
origin  git@github.com:username/repo.git (push)
```

Если там HTTPS — замени на SSH:

```bash
git remote set-url origin git@github.com:username/repo.git

```

Можно попробовать push(ить)!

## Если не работает, то просмотри следующие рекомендации

### Проверь, добавлен ли SSH-ключ в агент
Убедись, что ssh-agent запущен и твой ключ добавлен:
```bash
eval $(ssh-agent)
ssh-add ~/.ssh/id_ed25519
```
(Если ты указал другое имя при создании ключа — подставь его.)

### Проверка конфигурации SSH (~/.ssh/config)

Пример содержимого для GitHub может быть таким:
```bash
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
```
Это важно, чтобы Git знал, какой ключ использовать при подключении к GitHub (или другому хосту).

### Проверь, работает ли SSH с Git
Для GitHub:
```bash
ssh -T git@github.com
```
Если всё верно, увидишь приветствие типа:
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```