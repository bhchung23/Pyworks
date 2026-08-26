import random
import time
import tkinter as tk
from tkinter import messagebox


class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("영어 타자 게임")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.sentences = [
            "All men are created equal.",
            "Give me liberty, or give me death!",
            "I came, I saw, I conquered.",
            "The die is cast.",
            "To be, or not to be.",
            "Knowledge is power.",
            "The only thing we have to fear is fear itself.",
            "That government of the people, by the people, for the people.",
            "Four score and seven years ago.",
            "I have not yet begun to fight.",
            "Cogito, ergo sum.",
            "Veni, vidi, vici.",
            "The unexamined life is not worth living.",
            "We hold these truths to be self-evident.",
            "Ask not what your country can do for you."
        ]

        self.current_sentence = ""
        self.start_time = None
        self.running = False
        self.score = 0
        self.remaining_time = 60

        self.title_label = tk.Label(
            root,
            text="영어 타자 게임",
            font=("맑은 고딕", 24, "bold")
        )
        self.title_label.pack(pady=15)

        self.info_label = tk.Label(
            root,
            text="시작 버튼을 눌러 게임을 시작하세요.",
            font=("맑은 고딕", 12)
        )
        self.info_label.pack(pady=5)

        self.time_label = tk.Label(
            root,
            text="남은 시간: 60초",
            font=("맑은 고딕", 12),
            fg="red"
        )
        self.time_label.pack()

        self.sentence_label = tk.Label(
            root,
            text="",
            font=("Arial", 17),
            wraplength=650,
            fg="blue"
        )
        self.sentence_label.pack(pady=25)

        self.answer_entry = tk.Entry(
            root,
            font=("Arial", 16),
            width=55,
            state="disabled"
        )
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

        self.score_label = tk.Label(
            root,
            text="점수: 0",
            font=("맑은 고딕", 12)
        )
        self.score_label.pack(pady=5)

        self.start_button = tk.Button(
            root,
            text="게임 시작",
            font=("맑은 고딕", 12),
            width=15,
            command=self.start_game
        )
        self.start_button.pack(pady=15)

    def start_game(self):
        self.score = 0
        self.remaining_time = 60
        self.running = True
        self.start_time = time.time()

        self.score_label.config(text="점수: 0")
        self.time_label.config(text="남은 시간: 60초")
        self.info_label.config(text="문장을 정확하게 입력한 후 Enter를 누르세요.")

        self.answer_entry.config(state="normal")
        self.answer_entry.delete(0, tk.END)
        self.start_button.config(state="disabled")

        self.show_next_sentence()
        self.answer_entry.focus_set()
        self.update_timer()

    def show_next_sentence(self):
        self.current_sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.current_sentence)

    def check_answer(self, event=None):
        if not self.running:
            return

        answer = self.answer_entry.get().strip()

        if answer == self.current_sentence:
            self.score += 1
            self.score_label.config(text=f"점수: {self.score}")
            self.info_label.config(text="정답입니다!")
            self.answer_entry.delete(0, tk.END)
            self.show_next_sentence()
        else:
            self.info_label.config(text="오답입니다. 다시 입력하세요.")

    def update_timer(self):
        if not self.running:
            return

        elapsed = int(time.time() - self.start_time)
        self.remaining_time = 60 - elapsed

        self.time_label.config(text=f"남은 시간: {self.remaining_time}초")

        if self.remaining_time <= 0:
            self.end_game()
        else:
            self.root.after(1000, self.update_timer)

    def end_game(self):
        self.running = False
        self.answer_entry.config(state="disabled")
        self.start_button.config(state="normal")
        self.info_label.config(text="게임이 끝났습니다.")

        messagebox.showinfo(
            "게임 종료",
            f"게임 종료!\n최종 점수: {self.score}점"
        )


if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()