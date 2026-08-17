import os
from flask import Flask, render_template

app = Flask(__name__)

SITE = {
    "github_url": "https://github.com/JaiY1",
    "linkedin_url": "https://www.linkedin.com/in/jai-yadav11/",
    "email": "jaiyadav@gmail.com",
}

PROJECTS = [
    {
        "index": "01",
        "name": "NBA Player Props Tool",
        "status_label": "Live",
        "tagline": "Ask any player's stats a plain-English question — NBA or WNBA, auto-detected.",
        "description": (
            "Search a player and ask things like “how often does he hit 3+ threes in "
            "the last 10 games?” and get a straight hit-rate answer, not a stat dump. "
            "It auto-detects NBA vs WNBA and switches leagues with no dropdown, excludes "
            "DNP/injury games from the denominator, and handles mid-season trades by only "
            "counting a player's current-team stint. Live sportsbook prop lines can be "
            "pulled in and checked against the same hit-rate logic."
        ),
        "stack": ["Flask", "SQLite", "ESPN API", "SharpAPI", "Railway"],
        "repo_url": "https://github.com/JaiY1/Nba-player-props-tool",
        "live_url": "https://nba-tool.up.railway.app",
    },
    {
        "index": "02",
        "name": "News Aggregator",
        "status_label": "Live",
        "tagline": "AI-summarized news digests across the topics you actually follow.",
        "description": (
            "Pulls stories from a set of sources, summarizes them with Claude, and "
            "assembles a personal digest instead of a raw feed to scroll through. A "
            "scheduler keeps digests current so there's always something fresh waiting "
            "rather than a manual refresh."
        ),
        "stack": ["Go", "Claude API", "Scheduler", "SQLite"],
        "repo_url": "https://github.com/JaiY1/News-Aggregator",
        "live_url": "https://news-aggregator-1.up.railway.app",
    },
    {
        "index": "03",
        "name": "Closet Manager",
        "status_label": "Live",
        "tagline": "An AI wardrobe that tags your clothes, learns your style, builds outfits, and shops the gaps.",
        "description": (
            "Drop in a photo and Claude Vision auto-tags type, color, and fit. Semantic "
            "search finds garments by meaning, not keywords, and a multi-agent "
            "coordinator answers free-text questions about the wardrobe. A style profile "
            "written from actual wear history personalizes outfit suggestions, and a "
            "Gemini image pipeline generates garment cutouts and a virtual try-on. A "
            "shopping agent flags genuine gaps, searches live listings within budget, "
            "and scores each result against your style before it lands on a wishlist."
        ),
        "stack": ["Flask", "Claude API", "Gemini", "RAG", "ChromaDB", "Serper"],
        "repo_url": "https://github.com/JaiY1/closet-manager",
        "live_url": "https://closet-manager.up.railway.app",
    },
]

SKILLS = [
    {"group": "Backend", "skills": ["Python", "Flask", "Gunicorn", "SQLite"]},
    {"group": "AI / ML", "skills": ["Claude API", "Gemini", "RAG", "ChromaDB"]},
    {"group": "Data / APIs", "skills": ["ESPN API", "SharpAPI", "Serper", "Schedulers"]},
    {"group": "Infra", "skills": ["Docker", "Railway", "REST", "Git"]},
]


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS, skills=SKILLS, site=SITE)


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", host="0.0.0.0",
             port=int(os.environ.get("PORT", 5003)))
