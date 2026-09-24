# 2 хостинга в 1 сайте — безопасные примеры

Production source и реальные server identifiers не публикуются. Здесь показан принцип: provider-specific детали остаются за единым интерфейсом.

## Что посмотреть

- [provider_adapter.py](provider_adapter.py) — единая модель двух провайдеров;
- [health_api.py](health_api.py) — агрегирование статуса.

## Реальная приватная структура

```text
apps/boberchik-vpn/
├── vpn_admin.py
├── vpn_cabinet_ext.py
├── full_template.py
├── vpn-admin.html
└── vpn-cabinet.html
```

[← Вернуться к кейсу](../../docs/unified-vps-panel.md)
