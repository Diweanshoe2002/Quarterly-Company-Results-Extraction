from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from ListOfFinancialMetric import ListOfFinancialMetric
from langchain_groq import ChatGroq
import os
class LLMResponseService:
    def __init__(self):
        os.environ["GROQ_API_KEY"] = "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"
        self.llm = ChatGroq(model_name="llama-3.1-70b-versatile", api_key=os.environ["GROQ_API_KEY"])
    def compile_template_and_get_llm_response(self, extracted_text):
        preamble = (
            "You're seeing the financial statement for a company and your job is to accurately extract the Total income, Total expense, PBT, and PAT.")
        postamble = "Do not include any explanation in the reply. Only include the extracted information in the reply."
        system_template = "{preamble}"
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
        human_template = "{format_instructions}\n\n{extracted_text}\n\n{postamble}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        parser = PydanticOutputParser(pydantic_object=ListOfFinancialMetric)

        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        request = chat_prompt.format_prompt(preamble=preamble,
                                            format_instructions=parser.get_format_instructions(),
                                            extracted_text=extracted_text,
                                            postamble=postamble).to_messages()
        response = self.llm.invoke(request)
        return response.content
