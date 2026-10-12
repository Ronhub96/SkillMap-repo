from flask import Flask, render_template, request, redirect, url_for
from career_engine import (
    get_all_careers,
    get_career_by_id,
    search_careers,
    ALL_CATEGORIES
)
from database import ALL_STREAMS, POPULAR_DEGREES

app = Flask(__name__)


@app.route("/")
def home():
    """Homepage / Dashboard route displaying overview, hero, and highlights."""
    featured_careers = get_all_careers()[:3]
    return render_template(
        "index.html",
        featured_careers=featured_careers,
        categories=ALL_CATEGORIES
    )


@app.route("/careers")
def careers():
    """
    Career catalogue route with Python-powered search, degree (BA, B.Com, BCA, etc.), and stream filters.
    """
    query = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    stream = request.args.get("stream", "").strip()
    degree = request.args.get("degree", "").strip()

    careers_list = search_careers(
        query=query,
        category=category,
        stream=stream,
        degree=degree
    )

    return render_template(
        "careers.html",
        careers=careers_list,
        query=query,
        selected_category=category,
        selected_stream=stream,
        selected_degree=degree,
        categories=ALL_CATEGORIES,
        streams=ALL_STREAMS,
        popular_degrees=POPULAR_DEGREES
    )


@app.route("/career/<career_id>")
def career_detail(career_id):
    """
    Dynamic career pathway & roadmap route.
    Displays required skills, qualifying degrees, and step-by-step milestones.
    """
    career = get_career_by_id(career_id)
    if not career:
        return redirect(url_for("careers"))

    return render_template("career_detail.html", career=career)


if __name__ == "__main__":
    app.run(debug=True)