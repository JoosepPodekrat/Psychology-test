import csv
from psychopy import visual, event, core

def read_example_words(file_path):
    examples = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            examples.append(row)
    return examples
def write_results(file_path, answers):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    empty_row_index = None
    for i, row in enumerate(rows):
        if all(cell == '' for cell in row):
            empty_row_index = i
            break

    if empty_row_index is None:
        empty_row_index = len(rows)
        rows.append([''] * 3) 

    column_index = 0
    while column_index < len(rows[empty_row_index]) and rows[empty_row_index][column_index] != '':
        column_index += 1

    for j in range(0, len(answers), 3):
        for k in range(3):
            if j + k < len(answers):
                if column_index < len(rows[empty_row_index]):
                    rows[empty_row_index][column_index] = answers[j + k]
                    column_index += 1
                else:
                    rows[empty_row_index].append(answers[j + k])
                    column_index += 1

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

example_words = read_example_words('example_words.csv')

win = visual.Window(color=(1, 1, 1), units='pix', fullscr=True)

responses = []
explanation_box = visual.TextStim(win,text='you will be given 3 words, and your task is to find a word that is related to all three of these.',pos=(0, 200), color=(-1, -1, -1))
text_box_1 = visual.TextStim(win, text='sleeping', pos=(0, 100), color=(-1, -1, -1))
text_box_2 = visual.TextStim(win, text='trash', pos=(0, 0), color=(-1, -1, -1))
text_box_3 = visual.TextStim(win, text='bean', pos=(0, -100), color=(-1, -1, -1))
editable_box = visual.TextStim(win, text='', pos=(0, -200), height=30, color=(-1, -1, -1))
editable_box_explanation = visual.TextStim(win, text='Your text will go here: ', pos=(-300, -200), height=30, color=(-1, -1, -1))

continue_button = visual.TextStim(win, text='Press Enter to move on, or escape to close the application at any point, this will void the data.', pos=(0, -300), color=(-1, -1, -1))

slider_background = visual.Rect(win, width=400, height=30, pos=(400, 0), fillColor=(0.8, 0.8, 0.8), lineColor=None)
slider = visual.Slider(win, ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], pos=(400, 0), size=(300, 20), style='rating', color=(0, 0, 0), markerColor=(1, 0, 0))
slider_text = visual.TextStim(win, text='How confident are you in understanding the test? (1 - no confidence, 10 - very confident)', pos=(400, 50), color=(-1, -1, -1))

user_input = ""
slider.reset()
exit_outer_loop = False
while True:
    explanation_box.draw()
    editable_box_explanation.draw()
    text_box_1.draw()
    text_box_2.draw()
    text_box_3.draw()
    editable_box.setText(user_input)
    editable_box.draw()
    continue_button.draw()
    slider_background.draw()
    slider.draw()
    slider_text.draw()
    win.flip()

    keys = event.getKeys()

    if 'escape' in keys:
        win.close()
        core.quit()

    for key in keys:
        if key == 'return':
            if user_input and slider.getRating() is not None:
                exit_outer_loop = True
                break
        elif key == 'backspace':
            user_input = user_input[:-1]
        elif key not in ['lshift', 'rshift', 'lctrl', 'rctrl', 'lalt', 'ralt', 'capslock', 'numlock', 'scrolllock'] and key != 'space':
            user_input += key.lower()

    if exit_outer_loop:
        break
exit_outer_loop = False

for text_1, text_2, text_3, expected_answer in example_words:
    text_box_1 = visual.TextStim(win, text=text_1, pos=(0, 100), color=(-1, -1, -1))
    text_box_2 = visual.TextStim(win, text=text_2, pos=(0, 0), color=(-1, -1, -1))
    text_box_3 = visual.TextStim(win, text=text_3, pos=(0, -100), color=(-1, -1, -1))

    editable_box = visual.TextStim(win, text='', pos=(0, -200), height=30, color=(-1, -1, -1))

    continue_button = visual.TextStim(win, text='Press Enter to submit your answer', pos=(0, -300), color=(-1, -1, -1))

    slider_background = visual.Rect(win, width=400, height=30, pos=(400, 0), fillColor=(0.8, 0.8, 0.8), lineColor=None)
    slider = visual.Slider(win, ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], pos=(400, 0), size=(300, 20), style='rating', color=(0, 0, 0), markerColor=(1, 0, 0))
    slider_text = visual.TextStim(win, text='How confident are you in your answer? (1 - no confidence, 10 - very confident)', pos=(400, 50), color=(-1, -1, -1))

    user_input = ""
    slider.reset()
    exit_outer_loop = False

    while True:
        text_box_1.draw()
        text_box_2.draw()
        text_box_3.draw()
        editable_box.setText(user_input)
        editable_box.draw()
        continue_button.draw()
        slider_background.draw()
        slider.draw()
        slider_text.draw()
        win.flip()

        keys = event.getKeys()

        if 'escape' in keys:
            win.close()
            core.quit()

        for key in keys:
            if key == 'return':
                if user_input and slider.getRating() is not None:
                    exit_outer_loop = True
                    break
            elif key == 'backspace':
                user_input = user_input[:-1]
            elif key not in ['lshift', 'rshift', 'lctrl', 'rctrl', 'lalt', 'ralt', 'capslock', 'numlock', 'scrolllock'] and key != 'space':
                user_input += key.lower()

        if exit_outer_loop:
            break
    exit_outer_loop = False
    slider_value = slider.getRating()
    responses.append(user_input)
    responses.append(slider_value)


    correct_answer_screen = visual.TextStim(win, text=f'The correct answer was: ' + expected_answer, pos=(0, 100), color=(-1, -1, -1))
    slider_background = visual.Rect(win, width=400, height=30, pos=(400, 0), fillColor=(0.8, 0.8, 0.8), lineColor=None)
    slider = visual.Slider(win, ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], pos=(400, 0), size=(300, 20), style='rating', color=(0, 0, 0), markerColor=(1, 0, 0))
    slider_text = visual.TextStim(win, text='How strong was your AHA moment? (1 - did not feel it, 10 - life changing)', pos=(400, 50), color=(-1, -1, -1))
    continue_button2 = visual.TextStim(win, text='Press Enter to submit your answer', pos=(0, -300), color=(-1, -1, -1))
    
    while True:
        continue_button2.draw()
        correct_answer_screen.draw()
        slider_background.draw()
        slider.draw()
        slider_text.draw()
        win.flip()
        keys = event.getKeys()
        for key in keys:
            if key == 'return':
                if slider.getRating() is not None:
                    exit_outer_loop = True
                    responses.append(slider.getRating())
                    break
        if exit_outer_loop:
            break
write_results('TestData.csv', responses)
while True:
    keys = event.getKeys()

    if 'escape' in keys:
        win.close()
        core.quit()
    correct_answer_screen = visual.TextStim(win, text=f'Its now safe to close the test. Thank you for taking part in it.', pos=(0, 100), color=(-1, -1, -1))
    correct_answer_screen2 = visual.TextStim(win, text=f'Press Escape to quit.', pos=(0, 200), color=(-1, -1, -1))
    correct_answer_screen2.draw()
    correct_answer_screen.draw()
    win.flip()