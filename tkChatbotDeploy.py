from tkinter import *
import pandas as pd


def get_data(path):
    d = pd.read_csv(path)
    d.index = d.index + 1
    return d


data = get_data(r'C:\Users\MMM-SM\21Pypractice\chatbot_project\Deploy\Questions_ans.csv')
# topic = pd.DataFrame(zip(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], data['Labels'].unique()),
#                      columns=['Topic_Labels', 'Topics'])  # columns=['Topics']
# topic.set_index('Topic_Labels', inplace=True)

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

topics = {'A': 'Hierarchial', 'B': 'k_means', 'C': 'PCA', 'D': 'Random_forest', 'E': 'SVM',
          'F': 'KNN', 'G': 'NAÏVE BAYES', 'H': 'Decision tree', 'I': 'Logistic'}
topic = "t"
questions = data.copy()


def get_response(msg):
    # questions = {'A': list(range(21)), 'B': list(range(21, 42)), 'C': list(range(42, 52)),
    #              'D': list(range(52, 74)), 'E': list(range(74, 89)), 'F': list(range(89, 109)),
    #              'G': list(range(109, 121)), 'H': list(range(121, 146)), 'I': list(range(146, 166))}
    try:
        if msg == 'hi':
            return f'''Hello..... Choose the topic you want to study
                    
                    A :- HIRARCHICAL
                    B :- K-MEANS
                    C :- PCA
                    D :- RANDOM FOREST
                    E :- SVM
                    F :- KNN
                    G :- NAIVE BAYES
                    H :- DECISION TREE
                    I :- LOGISTIC'''
        elif msg == 'x':
            return f"Bye, See you next time"
        elif msg == '#':
            return f'''
                    A :- HIRARCHICAL
                    B :- K-MEANS
                    C :- PCA
                    D :- RANDOM FOREST
                    E :- SVM
                    F :- KNN
                    G :- NAIVE BAYES
                    H :- DECISION TREE
                    I :- LOGISTIC
    
        Select one option
                or
        Select "x" to exit
                or
        Select "?" for questions list'''
        elif msg.upper() in topics:
            global topic
            topic = str(topics[msg.upper()])
            global questions
            questions = data[data.Labels == topic]
            return f'''list of Questions under the topic {topic}
             
    {data[data.Labels == topics[msg.upper()]].loc[:, 'Questions']}
    
    Select any one question number for Answer'''
        elif msg == '?':
            return f'''list of Questions under the topic {topic}
             
    {questions.loc[:, 'Questions']}
    
    Select any one question number for Answer'''
        elif int(msg) in range(167):
            return f'''Question no {int(msg)} : {questions.loc[int(msg), 'Questions']} 
            
    Answer: {data.loc[int(msg), 'Answers']}'''
        else:
            return f'''Sorry, The Question number is our of range...
            Select "#" for Topics list
            Select "?" for Questions from the TOPIC
            Select "x" to exit'''

    except:
        return f'''Sorry, You selected a Wrong Option...
Select "#" for Topics list
Select "?" for Questions from the TOPIC
Select "x" to exit'''


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=650, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text='''Welcome to "SARVAGNYA"''', font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        head_label1 = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                            text='Your personal DS interview prep tool', font=FONT, pady=10)
        head_label1.place(relwidth=1, rely=0.05)
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.12, relheight=0.01)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.77, relwidth=1, rely=0.13)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.97)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=60)
        bottom_label.place(relwidth=1, rely=0.895)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.77, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        # if not msg:
        #     return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"Sarvagnya: \n{get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        # self.text_widget.insert(END, 'Select any one option\n\n')
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
