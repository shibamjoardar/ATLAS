from agent import ask_agent

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("ATLAS: Goodbye!")
        break

    answer = ask_agent(user_input)

    print("\nATLAS:", answer)