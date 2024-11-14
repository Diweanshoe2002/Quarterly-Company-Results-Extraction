from PdfDataExtracter import PdfDataExtracter
from LLMResponseService import LLMResponseService

pdfExtracterobj = PdfDataExtracter()
pdfExtracterobj.extract_text_from_pdf()
llm_service= LLMResponseService()
print(llm_service.compile_template_and_get_llm_response(pdfExtracterobj.text))


