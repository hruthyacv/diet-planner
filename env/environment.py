import random

class DietEnv:
    def __init__(self):
        self.state = None

    def reset(self):
        self.state = {
            "goal": random.choice(["weight_loss", "muscle_gain"]),
            "calories_target": random.choice([1500, 1800, 2000]),
            "diet_type": random.choice(["veg", "non_veg"]),
            "budget": random.choice(["low", "medium"]),
        }
        return self.state

    def step(self, action):
        reward = self.evaluate(action)
        done = True
        return self.state, reward, done, {}

    def evaluate(self, action):
        reward = 0

        # Calorie match
        if action.get("calories", 0) in range(
            self.state["calories_target"] - 200,
            self.state["calories_target"] + 200
        ):
            reward += 0.4

        # Diet type check
        if self.state["diet_type"] == "veg":
            if "chicken" not in str(action) and "egg" not in str(action):
                reward += 0.3
        else:
            reward += 0.3

        # Meal diversity
        meals = [
            action.get("breakfast"),
            action.get("lunch"),
            action.get("dinner")
        ]

        if len(set(meals)) == 3:
            reward += 0.3

        return round(reward, 2)