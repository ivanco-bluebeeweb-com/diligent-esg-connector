# Diligent ESG Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** Diligent API Key / OAuth 2.0 Client Credentials
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `GET /esg/v1/metrics`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.
