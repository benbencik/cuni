import numpy as np

def show_animation(agent, env, steps=200, episodes=1):
    ''' Pomocna funkce, ktera zobrazuje chovani zvoleneho agenta v danem 
    prostredi.
    Parameters
    ----------
    agent: 
        Agent, ktery se ma vizualizivat, musi implementovat metodu
        act(observation, reward, done)
    env:
        OpenAI gym prostredi, ktere se ma pouzit
    
    steps: int
        Pocet kroku v prostredi, ktere se maji simulovat
    
    episodes: int
        Pocet episod, ktere se maji simulovat - kazda a pocet kroku `steps`.
    '''
    for i in range(episodes):
        obs = env.reset()
        done = False
        R = 0
        t = 0
        r = 0
        while not done and t < steps:
            env.render()
            action = agent.act(obs, r, done)
            obs, r, done, _ = env.step(action)
            R += r
            t += 1
        agent.reset()

def moving_average(x, n):
    weights = np.ones(n)/n
    return np.convolve(np.asarray(x), weights, mode='valid')