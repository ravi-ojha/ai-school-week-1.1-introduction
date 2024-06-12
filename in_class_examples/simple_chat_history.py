from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chat = ChatOpenAI()

messages =  [
            HumanMessage(
                content="Translate this sentence from English to French: I love programming."
            ),
            AIMessage(content="J'adore la programmation."),
            HumanMessage(content="What did you just say?"),
        ]

result = chat.invoke(messages)

messages.append(result)
print(messages)

# Continue the conversation
# Try: Can you translate that phrase into Spanish?

while True:
      prompt = input("Prompt: ")
      messages.append(HumanMessage(content=prompt))

      result = chat.invoke(messages)
      
      messages.append(result)
      print(messages)
