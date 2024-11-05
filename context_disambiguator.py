class ContextDisambiguator:
    """
    This class implements a context disambiguation algorithm to differentiate 
    between the context of "Apple" as a fruit and as a company.
    """
    
    def __init__(self):
        # Define keywords for disambiguation
        self.fruit_keywords = {"fruit", "food", "orchard", "eating", "taste"}
        self.company_keywords = {"technology", "device", "mac", "iphone", "computer"}

    def disambiguate(self, text):
        """
        Disambiguates "Apple" context in the given text.
        
        Parameters:
        text (str): Input text containing "Apple" with ambiguous meaning.

        Returns:
        str: Returns the identified context: 'Apple (Fruit)', 'Apple (Company)', or 'Uncertain context'.
        """
        text_lower = text.lower()
        if any(keyword in text_lower for keyword in self.fruit_keywords):
            return "Apple (Fruit)"
        elif any(keyword in text_lower for keyword in self.company_keywords):
            return "Apple (Company)"
        else:
            return "Uncertain context"
