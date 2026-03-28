def hard_task(state, action):
    diet_ok = state["diet_type"] == "non_veg" or (
        "chicken" not in str(action) and "egg" not in str(action)
    )

    calorie_ok = abs(action["calories"] - state["calories_target"]) < 200

    meals = [
        action.get("breakfast"),
        action.get("lunch"),
        action.get("dinner")
    ]

    diversity = len(set(meals)) == 3

    return diet_ok and calorie_ok and diversity