import random

def magic_8_ball():
    responses = [
        "It is certain.",
        "Without a doubt.",
        "You may rely on it.",
        "Yes, definitely.",
        "It is decidedly so.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    print("Welcome to the Magic 8-Ball!")
    while True:
        question = input("\nAsk a yes/no question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            print("Goodbye! May your future be bright!")
            break
        elif question.strip() == '':
            print("Please ask a question.")
        else:
            answer = random.choice(responses)
            print("Magic 8-Ball says:", answer)

if __name__ == "__main__":
    magic_8_ball()
