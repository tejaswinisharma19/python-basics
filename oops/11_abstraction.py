from abc import ABC, abstractmethod

class DocumentProcessor(ABC):
    @abstractmethod
    def process(self):
        pass
    
class PDFProcessor(DocumentProcessor):
    def process(self):
        print("PDF document is being processed.")
        
class DOCXProcessor(DocumentProcessor):
    def process(self):
        print("DOCX document is being processed.")
        
class TXTProcessor(DocumentProcessor):
    def process(self):
        print("TXT document is being processed.")
        
documents = [PDFProcessor(),DOCXProcessor(),TXTProcessor()]

for document in documents:
    document.process()
    