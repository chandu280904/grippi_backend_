from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Grippi Campaign Analytics API")

# Allow CORS so frontend can fetch data from localhost or deployed domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, replace * with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base campaigns data
BASE_CAMPAIGNS = [
    {"id": 1, "name": "Summer Sale", "status": "Active"},
    {"id": 2, "name": "Black Friday", "status": "Paused"},
    {"id": 3, "name": "Winter Deals", "status": "Active"},
    {"id": 4, "name": "Spring Promo", "status": "Active"},
    {"id": 5, "name": "Cyber Monday", "status": "Paused"},
    {"id": 6, "name": "Holiday Blast", "status": "Active"},
    {"id": 7, "name": "Flash Sale", "status": "Paused"},
    {"id": 8, "name": "New Year Promo", "status": "Active"},
    {"id": 9, "name": "Back to School", "status": "Paused"},
    {"id": 10, "name": "Mega Discount", "status": "Active"},
]

@app.get("/campaigns")
async def get_campaigns(status: str = Query(None, description="Filter by status: Active or Paused")):
    campaigns = []

    for c in BASE_CAMPAIGNS:
        # Randomize clicks, cost, impressions each time
        campaign = {
            "id": c["id"],
            "name": c["name"],
            "status": c["status"],
            "clicks": random.randint(100, 500),
            "cost": round(random.uniform(20, 100), 2),
            "impressions": random.randint(1000, 5000)
        }
        campaigns.append(campaign)

    # Apply filter if provided
    if status in ["Active", "Paused"]:
        campaigns = [c for c in campaigns if c["status"] == status]

    return campaigns
