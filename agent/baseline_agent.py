def baseline_agent(state):
    if state["diet_type"] == "veg":
        return {
            "breakfast": "milk + banana",
            "lunch": "rice + dal",
            "dinner": "roti + paneer",
            "calories": state["calories_target"]
        }
    else:
        return {
            "breakfast": "eggs + toast",
            "lunch": "rice + chicken",
            "dinner": "roti + egg curry",
            "calories": state["calories_target"]
        }