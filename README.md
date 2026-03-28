# Diet Planner OpenEnv

## Description
This project simulates a real-world diet planning environment where an AI agent generates meal plans.

## State
- goal
- calories_target
- diet_type
- budget

## Action
- breakfast
- lunch
- dinner
- calories

## Reward
- Calorie match: 0.4
- Diet type match: 0.3
- Meal diversity: 0.3

## Tasks
- Easy: calorie match
- Medium: calorie + diet
- Hard: calorie + diet + diversity

## Run
```bash
python main.py