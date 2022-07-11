import turtle
import pandas

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

text = turtle.Turtle()
text.hideturtle()
text.penup()

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
revealed_states = []
unrevealed_states = []

while len(revealed_states) < 50:
    answer_state = screen.textinput(title=f"{len(revealed_states)}/50 States correct",
                                    prompt="Try to guess a state's name.").title()

    if answer_state == "Exit" or answer_state == "Quit":
        for state in all_states:
            if state not in revealed_states:
                unrevealed_states.append(state)

        new_data = pandas.DataFrame(unrevealed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        revealed_states.append(answer_state)
        state_data = data[data['state'] == answer_state]
        text.goto(int(state_data['x']), int(state_data['y']))
        text.write(answer_state)
