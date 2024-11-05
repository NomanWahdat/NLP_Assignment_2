class PerformanceEvaluator:
    """
    This class calculates performance metrics such as accuracy, precision, and recall
    based on true positives, false positives, and false negatives.
    """

    def calculate_metrics(self, tp, fp, fn):
        """
        Calculates accuracy, precision, and recall.
        
        Parameters:
        tp (int): True positives
        fp (int): False positives
        fn (int): False negatives

        Returns:
        tuple: Returns a tuple containing (accuracy, precision, recall).
        """
        accuracy = tp / (tp + fp + fn) if (tp + fp + fn) else 0
        precision = tp / (tp + fp) if (tp + fp) else 0
        recall = tp / (tp + fn) if (tp + fn) else 0
        return accuracy, precision, recall
