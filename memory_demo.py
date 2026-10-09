from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from summarizer_langchain import model

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a friendly tutor."),
        MessagesPlaceholder("history"),
        ("human", "{question}"),
    ]
)

chain = prompt | model

history = [HumanMessage("My name is Aarav"), AIMessage("Hi, Aarav!")]
print(chain.invoke({"question": "What is my name?", "history": history}).content)