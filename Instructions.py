Instructions = """◉You will have 5 tries to guess the correct word.
◉ 🟥 - it highlights the fact that all the letters you've guessed are incorrect.
◉ 🟨 - it highlights the fact that that particular letter is in fact present in the word to be guessed, 
        but it is in the incorrect position.
◉ 🟩 - the letter you've guessed is actually present in the word and is in the correct position.
◉ If you want to see your score and remarks, open the 'User_record' file in the same directory as this one.
◉ Please do not alter this file, as it may affect the user experience.
◉ You can copy the social media share code, to compare your result with your friends"""

def instructions():
        print(Instructions)