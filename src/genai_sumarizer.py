
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-1.5-flash")

def summarize_player_data(player_summary: str) -> str:
    """
    Uses Gemini 1.5 Flash to generate a natural-language summary of a player's stats or model output.

    Args:
        player_summary (str): Plain text with a player's performance data and context.

    Returns:
        str: AI-generated natural language insight.
    """
    try:
        prompt = f"""You are a data analyst tasked with interpreting player performance.
        Generate a short, executive-level summary of this NHL player's performance:
        {player_summary}
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[ERROR] Gemini API call failed: {e}"
