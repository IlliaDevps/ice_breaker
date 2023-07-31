from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = ''' 
       Elon Reeve Musk is a business magnate and investor. He is the founder, chairman, CEO, and chief technology officer of SpaceX;
       angel investor, CEO and product architect of Tesla, Inc.; owner and CTO of Twitter; founder of the Boring Company; co-founder of Neuralink and OpenAI; 
       and president of the Musk Foundation     
'''
if __name__ == '__main__':
    print('hello LangChain')
    
    summary_template = '''
            given the information {information} about a person from i want you to create:
            1. a short summary
            2. two interesting facts about them
            '''
    summary_prompt_template = PromptTemplate (input_variables=['information'], template= summary_template)
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    chain = LLMChain (llm=llm,prompt=summary_prompt_template)
    print(chain.run(information=information) )
