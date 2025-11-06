import numpy as np
from numba import jit


@jit(nopython=True)
def simular_rodadas(rodadas)->int:
        rodadas_vencidas = 0
        for i in range(rodadas):
                total_steps = 0
                for i in range(100):
                    roll = np.random.randint(1, 7)
                    fall_roll = np.random.randint(1, 10001)

                    if fall_roll == 7:
                        total_steps = 0
                        
                    else:
                        if roll == 1 or roll == 2:
                            if total_steps > 0:
                                total_steps -= 1

                        elif roll == 3 or roll == 4 or roll == 5:
                                total_steps += 1   

                        else:
                            bonus_roll = np.random.randint(1, 7)
                            total_steps += bonus_roll
                if total_steps >= 60:
                    rodadas_vencidas +=1

        return rodadas_vencidas




total_rounds = 1000000
x = simular_rodadas(total_rounds)
print(x)
print(total_rounds)
print(x/total_rounds)
