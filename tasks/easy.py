def easy_task(state, action):
    return abs(action["calories"] - state["calories_target"]) < 200