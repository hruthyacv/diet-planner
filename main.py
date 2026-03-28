from env.environment import DietEnv
from agent.baseline_agent import baseline_agent

def run():
    env = DietEnv()

    state = env.reset()
    print("\nSTATE:")
    print(state)

    action = baseline_agent(state)
    print("\nACTION:")
    print(action)

    next_state, reward, done, _ = env.step(action)

    print("\nREWARD:", reward)

if __name__ == "__main__":
    run()