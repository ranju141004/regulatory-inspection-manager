# Regulatory Inspection Manager — AI Summary Card

## Project Overview

The Regulatory Inspection Manager is an AI-powered compliance inspection platform that helps organizations identify risks, generate recommendations, and create inspection reports automatically using AI.

AI services are powered using Flask and the Groq LLaMA-3.3-70B model.

---

# AI Endpoints

## 1. POST /describe

Generates an AI description for inspection issues.

### Example Input

```json
{
  "input_text": "Oil leakage near pressure valve"
}
```

### Example Output

```json
{
  "description": "Potential oil leakage detected near the pressure valve. Immediate inspection is recommended to prevent equipment failure.",
  "generated_at": "2026-05-02T10:30:00"
}
```

---

## 2. POST /recommend

Generates AI safety recommendations.

### Example Input

```json
{
  "input_text": "Damaged wiring found near control panel"
}
```

### Example Output

```json
[
  {
    "action_type": "Repair",
    "description": "Replace damaged electrical wiring immediately.",
    "priority": "HIGH"
  }
]
```

---

## 3. POST /generate-report

Generates complete AI inspection reports.

### Example Input

```json
{
  "input_text": "Missing safety signs and damaged wiring"
}
```

### Example Output

```json
{
  "title": "Inspection Safety Report",
  "summary": "Critical safety violations detected.",
  "recommendations": [
    "Install updated safety signs",
    "Repair damaged electrical wiring"
  ]
}
```

---

# AI Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | AI service language |
| Flask 3.x | REST API framework |
| Groq API | LLM inference |
| LLaMA-3.3-70B | AI model |
| Redis | AI response caching |
| flask-limiter | Rate limiting |
| Docker | Containerization |
| pytest | AI endpoint testing |

---

# Security Features

- Prompt injection protection
- Input sanitization
- HTML stripping
- Rate limiting (30 req/min)
- Error handling with fallback responses
- PII-safe prompt templates

---

# GitHub Repository

Frontend + Backend + AI Service:

https://github.com/YOUR-USERNAME/regulatory-inspection-manager

---

# AI Developer 2 Responsibilities

- Groq API integration
- Prompt tuning
- AI report generation
- Security review
- Pytest testing
- AI documentation
- Demo preparation

---

# Demo Notes

Health Endpoint:

GET /health

AI Features Demonstrated During Demo:

- AI Description Generation
- AI Recommendation Engine
- AI Report Generation
