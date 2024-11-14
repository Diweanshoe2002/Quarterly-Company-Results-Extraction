from llama_parse import LlamaParse

class PdfDataExtracter:
    text : list
    def extract_text_from_pdf(self):
        parser = LlamaParse(api_key="llx-xOLTMwkyGJp9qNJyTx8WgL7WMWH5YaW39Y1CWj8Yyq1UMlNe", result_type="markdown")
        self.text = parser.load_data("C:\\Users\\hp\\PycharmProjects\\PYFINPROJECT\\WIPRO.pdf")
        print(self.text)

