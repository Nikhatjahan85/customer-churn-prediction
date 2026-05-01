from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Churn Analytics API")

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- HEALTH ----------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "API running successfully"
    }

# ---------------- SCORE ENDPOINT ----------------
@app.post("/score")
def score(data: dict):

    # -------- SIMPLE LOGIC --------
    risk_score = 0

    if data["support_tickets"] > 3:
        risk_score += 20

    if data["nps_score"] < 5:
        risk_score += 25

    if data["monthly_usage_hours"] < 15:
        risk_score += 20

    if data["last_payment_days_ago"] > 15:
        risk_score += 20

    if data["sla_breaches"] > 1:
        risk_score += 15

    # -------- CONVERT TO PROBABILITY --------
    churn_prob = min(risk_score / 100, 1)

    # -------- SEGMENT --------
    if churn_prob < 0.30:
        segment = "Low"

    elif churn_prob < 0.70:
        segment = "Medium"

    else:
        segment = "High"

    # -------- RESPONSE --------
    return {
        "customer_id": data["customer_id"],
        "churn_prob": churn_prob,
        "segment": segment
    }

# ---------------- EXPLAIN ENDPOINT ----------------
@app.post("/explain")
def explain(data: dict):

    features = [
        {
            "feature": "Support Tickets",
            "impact": round(random.uniform(0.2, 1.0), 2)
        },
        {
            "feature": "NPS Score",
            "impact": round(random.uniform(-1.0, -0.2), 2)
        },
        {
            "feature": "Usage Hours",
            "impact": round(random.uniform(-0.8, 0.5), 2)
        },
        {
            "feature": "Late Payments",
            "impact": round(random.uniform(0.3, 1.2), 2)
        },
        {
            "feature": "SLA Breaches",
            "impact": round(random.uniform(0.2, 0.9), 2)
        }
    ]

    return {
        "top_features": features
    }

# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {
        "message": "Churn Analytics API is Live"
    }