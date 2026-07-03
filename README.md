# Candidate Screening & Assessment Bot

An AI-powered recruitment automation tool that screens candidates and conducts Voice & Aptitude (V&A) assessments — reducing manual recruiter effort and cutting hiring costs.

---

## Problem Statement

Provana's Talent Acquisition team relies on manual effort for resume screening and V&A assessments, requiring 3 recruiters + 1 V&A resource. This creates a capacity ceiling and limits hiring scale. This bot automates that end-to-end.

---

## Features

- **Resume Screening** — AI-based JD matching, auto-shortlist/reject with reasons
- **Aptitude Assessment** — Timed MCQ tests, randomized question bank, auto-scoring
- **Voice Assessment** — Speech-to-text analysis for communication quality
- **Candidate Notifications** — WhatsApp/email updates at each stage
- **Recruiter Dashboard** — Pipeline view, scores, recordings, one-click scheduling
- **Admin Panel** — Configure cut-offs, manage question bank, view reports

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python (FastAPI) |
| AI/LLM | Claude API (Anthropic) |
| Voice | Deepgram |
| Frontend | React |
| Database | PostgreSQL |
| Notifications | WhatsApp Business API |

---

## Project Structure

```
Candidate-Screening-Assessment-Bot/
├── backend/
│   ├── app/
│   │   ├── api/routes/        # screening, assessment, dashboard
│   │   ├── core/              # config, security
│   │   ├── models/            # candidate, assessment
│   │   ├── services/          # screening, voice, aptitude, notification
│   │   ├── utils/             # llm helpers
│   │   └── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   └── src/
│       ├── pages/             # Dashboard, CandidateDetail
│       └── components/        # ScoreCard
├── assessments/
│   ├── voice/
│   └── aptitude/              # questions.json
└── docs/
    └── architecture.md
```

---

## Implementation Phases

| Phase | Scope | Target |
|-------|-------|--------|
| Phase 1 | Resume screening + Recruiter Dashboard | Q2 '26 |
| Phase 2 | Aptitude test engine | Q3 '26 |
| Phase 3 | Voice assessment + ATS sync | Q4 '26 |

---

## Expected Impact

- **₹51 Lakhs** annual cost savings
- **2x** assessment throughput with same manpower
- Eliminates dependency on 3 recruiters + 1 V&A resource

---

## Setup

```bash
# Backend
cd backend
pip install -r requirements.txt
cp .env.example .env   # fill in your API keys
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm start
```

---

## License

Internal use only — Provana © 2026
