# APPMacroGold — Institutional Macro + Gold Monitoring

Plataforma SaaS-style para monitoramento macroeconômico em tempo real com foco operacional em **XAUUSD**.

## Stack
- **Frontend:** Next.js 15, React, TypeScript, Tailwind, shadcn/ui, Recharts
- **Backend:** FastAPI, Python 3.12, SQLAlchemy, Pydantic, Redis (cache/pubsub), Celery (scheduler/queue)
- **DB:** PostgreSQL
- **Infra:** Docker Compose, Nginx (optional), GitHub Actions CI

## Funcionalidades
- Coleta contínua de dados para: XAUUSD, DXY, US10Y, BCOM, XAGUSD, HG, XPTUSD, Fed Funds
- Motor de tendência: EMA(9/21/50/200), RSI, ATR, volume, variação por janela
- Motor de confirmação macro/correlação com score 0–100
- Alertas:
  - Força compradora/vendedora confirmada
  - Possível exaustão/reversão
  - Spike/expansão de volatilidade
- Feed de alertas em tempo real via WebSocket
- Integração preparada para Telegram/e-mail/push

## Estrutura
```text
backend/
  app/
    api/
    core/
    db/
    engine/
    models/
    schemas/
    services/
    workers/
frontend/
  src/
infra/
```

## Rodando localmente
```bash
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend docs: http://localhost:8000/docs

## Notas de produção
- Configurar provedores de dados TradingView com credenciais seguras
- Ativar observabilidade (Prometheus + Grafana + Sentry)
- Habilitar autoscaling em workers conforme throughput de alertas
