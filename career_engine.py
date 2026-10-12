# career_engine.py - Python Recommendation & Search Engine
# Implements core business logic: skill-matching algorithm, career gap analysis, and queries.

from database import CAREERS_DATABASE, ALL_AVAILABLE_SKILLS, ALL_CATEGORIES


def get_all_careers():
    """Returns the full list of career records."""
    return CAREERS_DATABASE


def get_career_by_id(career_id):
    """
    Look up a single career by its unique slug identifier.
    Returns the career dictionary or None if not found.
    """
    for career in CAREERS_DATABASE:
        if career["id"] == career_id:
            return career
    return None


def search_careers(query="", category="", stream="", degree=""):
    """
    Filters careers by title, description, skills, category, academic stream, or target degree (BA, B.Com, BCA, etc.).
    Demonstrates Python string methods and list comprehensions.
    """
    filtered = CAREERS_DATABASE
    
    if degree and degree != "All":
        filtered = [c for c in filtered if degree.upper() in [d.upper() for d in c.get("eligible_degrees", [])]]

    if category and category != "All":
        filtered = [c for c in filtered if c["category"].lower() == category.lower()]

    if stream and stream != "All":
        filtered = [c for c in filtered if c.get("stream", "").lower() == stream.lower()]
        
    if query:
        q = query.lower().strip()
        filtered = [
            c for c in filtered
            if q in c["title"].lower()
            or q in c["description"].lower()
            or q in c.get("stream", "").lower()
            or any(q in s.lower() for s in c["skills"])
            or any(
                any(q in course.lower() for course in course_list)
                for course_list in c.get("education", {}).values()
            )
        ]
        
    return filtered


def match_skills(user_skills):
    """
    Core Python Algorithm: Skill-based Career Matching.
    
    Given a list of skills selected by the user:
    1. Normalizes skills for case-insensitive comparison.
    2. Uses Python set operations to find:
       - Matched skills (intersection)
       - Missing skills to learn (difference)
    3. Calculates match percentage: (matched / total_required) * 100
    4. Sorts careers in descending order by match percentage.
    
    Returns a ranked list of matched career result dictionaries.
    """
    if not user_skills:
        return []
    
    user_skill_set = {s.strip().lower() for s in user_skills if s.strip()}
    recommendations = []
    
    for career in CAREERS_DATABASE:
        required_skill_map = {s.lower(): s for s in career["skills"]}
        required_keys = set(required_skill_map.keys())
        
        # Python Set Math: Intersection & Difference
        matched_keys = required_keys.intersection(user_skill_set)
        missing_keys = required_keys.difference(user_skill_set)
        
        matched_skills = [required_skill_map[k] for k in matched_keys]
        missing_skills = [required_skill_map[k] for k in missing_keys]
        
        total_required = len(required_keys)
        match_percentage = round((len(matched_keys) / total_required) * 100) if total_required > 0 else 0
        
        recommendations.append({
            "career": career,
            "match_percentage": match_percentage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "match_count": len(matched_skills),
            "total_skills": total_required
        })
        
    # Sort recommendations by highest match percentage first
    recommendations.sort(key=lambda item: item["match_percentage"], reverse=True)
    return recommendations


def get_skill_recommendations_summary(user_skills):
    """
    Generates a personalized insight summary message based on user skills.
    Demonstrates Python conditional branching and formatting.
    """
    results = match_skills(user_skills)
    if not results:
        return None
        
    top_match = results[0]
    top_pct = top_match["match_percentage"]
    top_title = top_match["career"]["title"]
    
    if top_pct >= 70:
        insight = f"Outstanding alignment! You are already a strong candidate for {top_title}."
    elif top_pct >= 40:
        insight = f"Promising match! With a few key skills, you can pivot directly into {top_title}."
    else:
        insight = f"Foundational start! Exploring these pathways will guide your learning journey."
        
    return {
        "results": results,
        "top_match": top_match,
        "insight": insight,
        "all_skills": ALL_AVAILABLE_SKILLS,
        "categories": ALL_CATEGORIES
    }
