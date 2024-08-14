import pandas as pd
import turtle

states_data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
#screen.addshape(image)
#turtle.shape((image))


#create Turtle
turtle.penup()
turtle.hideturtle()
turtle.speed(1000000)


#Main
def check_answer(input):
    if input in states_data["state"].tolist():
        return(True)
    else:
        return(False)

def get_data(answer):
    index = states_data.index[states_data["state"] == answer]
    index = index[0]
    infos2 = (states_data._get_value(index, "state"), states_data._get_value(index, "x"),states_data._get_value(index, "y"))
    print(infos2)
    return(infos2)


def write(infos, answer):
    state, x, y = infos
    turtle.goto(x, y)
    turtle.write(answer, align="center")

def states_to_learn(list_known, all_states):
    learn = all_states
    for state in list_known:
        learn.remove(state)
    pd.DataFrame(learn, columns=["state"]).to_csv("states_to_learn")


def main_loop():
    game_on = True
    score = 0
    states_list = []
    while game_on:
        answer = str(screen.textinput(title=f"{len(states_list)} out of {len(states_data['state'])}", prompt="Whats another state's name?")).capitalize()
        if answer == "Exit":
            states_to_learn(states_list, states_data["state"].tolist())
            break
        if answer in states_list:
            continue
        else:
            check_answer(answer)
            write(get_data(answer), answer)
            states_list.append(answer)
            score += 1

main_loop()
screen.exitonclick()