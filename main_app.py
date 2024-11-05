import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import tkinter as tk
from context_disambiguator import ContextDisambiguator
from sentiment_analyzer import SentimentAnalyzer
from performance_evaluator import PerformanceEvaluator

class AdvancedAssignment2App:
    """
    This class defines the main GUI application for Assignment 2 tasks, including
    context disambiguation, sentiment analysis, and performance evaluation.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Assignment 2")
        self.root.geometry("800x600")

        # Initialize task-specific classes
        self.disambiguator = ContextDisambiguator()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.evaluator = PerformanceEvaluator()

        # Tabbed layout
        self.tabs = ttk.Notebook(root, bootstyle="dark")
        self.tabs.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        self.create_disambiguation_tab()
        self.create_sentiment_tab()
        self.create_evaluation_tab()

    def create_disambiguation_tab(self):
        frame = ttk.Frame(self.tabs, padding=20)
        self.tabs.add(frame, text="Context Disambiguation")

        lbl = ttk.Label(frame, text="Enter a sentence with 'Apple':", font=("Arial", 10))
        lbl.pack(anchor=W, pady=5)

        self.disamb_input = ttk.Text(frame, height=5, width=70)
        self.disamb_input.pack(fill=X, pady=5)

        process_btn = ttk.Button(frame, text="Disambiguate", command=self.process_disambiguation)
        process_btn.pack(pady=5)

        output_lbl = ttk.Label(frame, text="Output:", font=("Arial", 10))
        output_lbl.pack(anchor=W, pady=5)

        self.disamb_output = ttk.Text(frame, height=5, width=70, state="disabled")
        self.disamb_output.pack(fill=X, pady=5)

    def create_sentiment_tab(self):
        frame = ttk.Frame(self.tabs, padding=20)
        self.tabs.add(frame, text="Sentiment Analysis")

        lbl = ttk.Label(frame, text="Enter sentences for sentiment analysis:", font=("Arial", 10))
        lbl.pack(anchor=W, pady=5)

        self.sentiment_input = ttk.Text(frame, height=5, width=70)
        self.sentiment_input.pack(fill=X, pady=5)

        process_btn = ttk.Button(frame, text="Analyze Sentiment", command=self.process_sentiment)
        process_btn.pack(pady=5)

        output_lbl = ttk.Label(frame, text="Output:", font=("Arial", 10))
        output_lbl.pack(anchor=W, pady=5)

        self.sentiment_output = ttk.Text(frame, height=5, width=70, state="disabled")
        self.sentiment_output.pack(fill=X, pady=5)

    def create_evaluation_tab(self):
        frame = ttk.Frame(self.tabs, padding=20)
        self.tabs.add(frame, text="Performance Evaluation")

        lbl = ttk.Label(frame, text="Enter values for TP, FP, and FN:", font=("Arial", 10))
        lbl.pack(anchor=W, pady=5)

        self.tp_entry = ttk.Entry(frame, width=20)
        self.tp_entry.insert(0, "True Positives")
        self.tp_entry.pack(pady=5)

        self.fp_entry = ttk.Entry(frame, width=20)
        self.fp_entry.insert(0, "False Positives")
        self.fp_entry.pack(pady=5)

        self.fn_entry = ttk.Entry(frame, width=20)
        self.fn_entry.insert(0, "False Negatives")
        self.fn_entry.pack(pady=5)

        process_btn = ttk.Button(frame, text="Calculate Metrics", command=self.process_evaluation)
        process_btn.pack(pady=5)

        output_lbl = ttk.Label(frame, text="Output:", font=("Arial", 10))
        output_lbl.pack(anchor=W, pady=5)

        self.eval_output = ttk.Text(frame, height=5, width=70, state="disabled")
        self.eval_output.pack(fill=X, pady=5)

    def process_disambiguation(self):
        input_text = self.disamb_input.get("1.0", tk.END).strip()
        output = self.disambiguator.disambiguate(input_text)
        self.disamb_output.config(state="normal")
        self.disamb_output.delete("1.0", tk.END)
        self.disamb_output.insert(tk.END, output)
        self.disamb_output.config(state="disabled")

    def process_sentiment(self):
     input_text = self.sentiment_input.get("1.0", tk.END).strip().splitlines()
     output = self.sentiment_analyzer.analyze_sentiment(input_text)
     self.sentiment_output.config(state="normal")
     self.sentiment_output.delete("1.0", tk.END)
     self.sentiment_output.insert(tk.END, output)
     self.sentiment_output.config(state="disabled")

    def process_evaluation(self):
        tp = int(self.tp_entry.get())
        fp = int(self.fp_entry.get())
        fn = int(self.fn_entry.get())
        accuracy, precision, recall = self.evaluator.calculate_metrics(tp, fp, fn)
        
        output = f"Accuracy: {accuracy:.2f}\nPrecision: {precision:.2f}\nRecall: {recall:.2f}"
        self.eval_output.config(state="normal")
        self.eval_output.delete("1.0", tk.END)
        self.eval_output.insert(tk.END, output)
        self.eval_output.config(state="disabled")

# Run the GUI
def main():
    root = ttk.Window(themename="darkly")
    app = AdvancedAssignment2App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
