# n8n Automation — безопасный workflow

Пример показывает orchestration-паттерн без credential IDs, внутренних URL и production data.

## Файлы

- [workflow.example.json](workflow.example.json) — минимальный n8n workflow;
- [worker.py](worker.py) — Python-шаг, который удобно вызывать из workflow.

Смысл разделения: n8n управляет последовательностью и ветвлением, Python выполняет тестируемую прикладную логику.

[← Вернуться к кейсу](../../docs/n8n-automation.md)
