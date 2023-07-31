from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """ 
       Elon  Musk  
"""
if __name__ == "__main__":
    print("hello LangChain")

    summary_template = """
            given the information {information} about a person from i want you to create:
            1. a short summary
            2. two interesting facts about them
            """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    print(chain.run(information=information))
