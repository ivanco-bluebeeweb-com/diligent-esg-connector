# Diligent ESG Connector — Connector Discovery

**Category:** C48. Environmental, Social & Governance (ESG) Reporting  
**Vendor:** Diligent ESG  
**Official Website:** https://www.diligent.com/solutions/esg

## 1. Официальный API
- **Базовый URL API:** `https://api.diligent.com/esg/v1`
- **Поддерживаемая модель авторизации:** Diligent API Key / OAuth 2.0 Client Credentials

## 2. Архитектура сущностей
- Ключевые ресурсы платформы Diligent ESG:
  - ESG-метрики (/metrics)
  - опросники раскрытия информации (/questionnaires)
  - отчетные периоды (/periods)
  - бенчмарки

## 3. Требования к отказоустойчивости и безопасности
- Соблюдение вендорных лимитов запросов (Rate Limiting) с экспоненциальной задержкой.
- Строгая валидация Pydantic-схем на входе и выходе каждого запроса.
- Тестовая точка проверки подключения: `GET /esg/v1/metrics`.
