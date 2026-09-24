# Boberchik Infrastructure

[← Все проекты](../README.md) · [Код / примеры](../examples/boberchik-infrastructure/)

**Тип:** рабочая инфраструктура нескольких Linux-серверов
**Стек:** Linux · nginx · systemd · Bash · Python · GitHub Actions

## Задача

Хранить воспроизводимую часть серверной конфигурации отдельно от живого runtime-состояния и секретов, чтобы сервисы можно было проверять, переносить и восстанавливать.

## Что входит

- nginx-конфигурация;
- systemd services и timers;
- SSH-hardening, fail2ban и sysctl;
- deployment/configuration scripts;
- Python/Bash служебные утилиты;
- инвентаризация сервисов;
- backup/recovery;
- CI и secret scan.

## Архитектура

```mermaid
flowchart TD
    G[Git: safe configuration] --> CI[CI checks]
    G --> DEPLOY[Deploy scripts]
    DEPLOY --> S1[Linux server A]
    DEPLOY --> S2[Linux server B]
    S1 --> N1[nginx / systemd / apps]
    S2 --> N2[nginx / systemd / apps]
    BACKUP[Backup / recovery] --> S1
    BACKUP --> S2
    SECRET[Runtime secrets] -. not in Git .-> S1
    SECRET -. not in Git .-> S2
```

## Цикл изменения

```mermaid
flowchart LR
    CHANGE[Config change] --> CHECK[Secret + syntax checks]
    CHECK --> COMMIT[Git]
    COMMIT --> DEPLOY[Deploy]
    DEPLOY --> HEALTH[Health checks]
    HEALTH -->|OK| DONE[Done]
    HEALTH -->|Fail| ROLLBACK[Restore / rollback]
```

## Пример структуры

```text
.github/workflows/ci.yml
3x-ui/
├── README.md
├── install-vdsina.sh
└── provision-reality.py
apps/
├── boberchik-cloud/
├── boberchik-vpn/
├── mcp-gateway/
└── traffic-dashboard/
scripts/
└── secret-scan.sh
```

## Код / примеры

- [Health check script](../examples/boberchik-infrastructure/healthcheck.sh)
- [systemd service example](../examples/boberchik-infrastructure/example.service)
- [Папка примеров](../examples/boberchik-infrastructure/)

## Проверки

CI выполняет secret scan, shell syntax validation и Python compile checks. Scanner блокирует реальные `.env` и token-like значения, но допускает безопасные шаблоны `.env.example`.

## Что не хранится в Git

Рабочие базы, токены, ключи, client identifiers, cookies, sessions, certificates, логи и backup-архивы остаются вне публичного Git.

Production infrastructure repository остаётся приватным.
