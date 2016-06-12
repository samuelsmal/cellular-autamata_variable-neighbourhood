from collections import Counter
import random as rnd

def run_automata(
        number_of_cells=64,
        number_of_steps=32,
        fire_starting_threshold=0.1,
        size_fire_neighbourhood=1,
        size_alive_neihbourhood=2,
        size_growing_neighbourhood=1):
    """Simulation of a forest fire using a cellular automata with variable width."""

    # ca_curr = [(0 if rnd.random() < 0.5 else 1) for i in range(number_of_cells)]
    ca_curr = [0]*number_of_cells

    ca_curr[0] = 2
    ca_curr[1] = 1
    ca_curr[2] = 1
    ca_curr[3] = 0
    ca_curr[4] = 1

    ca_next = ca_curr[:]

    # dictionary maps the cell value to a symbol
    # 0: nothing
    # 1: alive
    # 2: on fire
    dic = {0:'_', 1:'*', 2:'~'}

    print(''.join([dic[e] for e in ca_next]))

    step = 1
    while step < number_of_steps:
        ca_next = []
        for i in range(0, number_of_cells):
            # starting a fire, if the tree is alive
            # this takes precedent
            # if ca_curr[i] == 1:
                # if rnd.random() < fire_starting_threshold:
                    # ca_next.append(2)
                    # continue

            fire_neighbourhood = ca_curr[max(0, i - size_fire_neighbourhood): i] \
                + ca_curr[i + 1:min(number_of_cells - 1, i + size_fire_neighbourhood + 1)]

            keeping_alive_neighbourhood = ca_curr[max(0, i - size_alive_neihbourhood): i] \
                + ca_curr[i + 1:min(number_of_cells - 1, i + size_alive_neihbourhood + 1)]

            growing_neighbourhood = ca_curr[max(0, i - size_growing_neighbourhood): i] \
                + ca_curr[i + 1:min(number_of_cells - 1, i + size_growing_neighbourhood + 1)]

            # tree alive but some sourounding tree is on fire
            if ca_curr[i] == 1 and Counter(fire_neighbourhood)[2] > 0:
                ca_next.append(2)
                continue

            if ca_curr[i] == 0 and sum(growing_neighbourhood) < 1:
                ca_next.append(1)
                continue

            # Keep at least on space free, otherwise overcrowding
            n = Counter(keeping_alive_neighbourhood)
            if ca_curr[i] == 1:
                if n[0] > 0:
                    ca_next.append(1)
                else:
                    ca_next.append(0)

                continue

            if ca_curr[i] == 2:
                ca_next.append(0)
                continue

            ca_next.append(ca_curr[i])

        # draw current cell state
        print(''.join([dic[e] for e in ca_next]))

        # update cell list
        ca_curr = ca_next[:]

        # step count
        step += 1


if __name__ == '__main__':
    run_automata()
