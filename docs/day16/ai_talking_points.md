# AI Talking Points — Regulatory Inspection Manager

## AI Stack

- Python 3.11
- Flask 3.x
- Groq API
- LLaMA 3.3 70B model
- Redis caching
- Docker containerized AI service

---

## What the AI Does

The AI service helps inspectors generate:

1. Inspection descriptions
2. Safety recommendations
3. Full inspection reports

The AI improves speed, consistency, and report quality.

---

## Endpoint 1 — /describe

Input:
- Inspection issue text

AI Output:
- Structured professional inspection description

Example:
Input:
"Damaged wiring near panel"

Output:
"Electrical wiring damage detected near the control panel creating potential fire and safety hazards."

---

## Endpoint 2 — /recommend

AI generates:
- Action recommendations
- Priority levels
- Safety guidance

Example:
- Replace damaged wiring
- Conduct electrical safety inspection
- Install warning signage

---

## Endpoint 3 — /generate-report

AI generates:
- Report title
- Executive summary
- Risk overview
- Key findings
- Recommendations

This helps inspectors create professional reports quickly.

---

## Prompt Engineering

We use carefully designed prompts to:
- Keep outputs professional
- Prevent hallucinations
- Ensure structured JSON responses
- Improve consistency

Prompts are stored in:
ai-service/prompts/

---

## AI Reliability Features

Implemented protections:
- Input validation
- Prompt injection detection
- Retry mechanism
- Error handling
- Fallback responses
- Rate limiting
- Redis caching

---

## Performance

Optimizations:
- Redis response cache
- Reduced AI latency
- Optimized prompts
- Fast Groq inference

Average response target:
Under 2 seconds

---

## Dockerized AI Service

The AI service runs independently inside Docker.

Benefits:
- Easy deployment
- Consistent environments
- Simple scaling
- Reliable demo setup

---

## Plain English Explanation

“The AI reads inspection issues written by users and converts them into professional safety documentation automatically.”