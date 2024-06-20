from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


safe_client = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)
ambitious_client = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

engineer_history = [
    SystemMessage(content="As a software engineer, explain how to create a CRUD application in Django. Keep it reall short."),
]

jack_history = [
    SystemMessage(content="As Jack Sparrow, you hear the explanation and responds with curiosity and a follow up question"),
]

reply = safe_client.invoke(engineer_history).content
engineer_history.append(AIMessage(content=reply))
print(f"Software Engineer: {reply}\n")
print("-" * 50, "\n")

jack_history.append(AIMessage(content=reply))
reply = ambitious_client.invoke(jack_history).content
engineer_history.append(HumanMessage(content=reply))

print(f"Jack Sparrow: {reply}\n")
print("-" * 50, "\n")

while True:
    reply = safe_client.invoke(engineer_history).content
    engineer_history.append(AIMessage(content=reply))
    print(f"Software Engineer: {reply}\n")
    print("-" * 50, "\n")

    jack_history.append(AIMessage(content=reply))
    reply = ambitious_client.invoke(jack_history).content
    engineer_history.append(HumanMessage(content=reply))
    print(f"Jack Sparrow: {reply}\n")
    print("-" * 50, "\n")

    prompt = input("Continue chat? (y/n): ")
    if prompt.lower() != "y":
        break
