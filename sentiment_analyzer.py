class SentimentAnalyzer:
    """
    This class implements a basic sentiment analysis algorithm by counting occurrences
    of positive and negative words in the input text.
    """

    def __init__(self):
        # Define simple positive and negative word lists
        self.positive_words = {"good", "happy", "love", "excellent", "fantastic", "great"}
        self.negative_words = {"bad", "sad", "hate", "terrible", "poor", "awful"}

    def analyze_sentiment(self, sentences):
        """
        Analyzes sentiment based on the count of positive and negative words.

        Parameters:
        sentences (list): List of sentences for analysis.

        Returns:
        str: 'Positive' if positive word count is higher, otherwise 'Negative'.
        """
        pos_count = 0
        neg_count = 0

        for sentence in sentences:
            # Count occurrences of positive and negative words
            words = sentence.lower().split()
            pos_count += sum(1 for word in words if word in self.positive_words)
            neg_count += sum(1 for word in words if word in self.negative_words)

        # Determine sentiment based on counts
        if pos_count > neg_count:
            return "Positive"
        elif neg_count > pos_count:
            return "Negative"
        else:
            return "Neutral"
