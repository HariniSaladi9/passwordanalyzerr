import sys
import os

# Ensure root directory is in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from analyzer.password_analyzer import analyze_password
from analyzer.wordlist_generator import generate_wordlist, save_wordlist
import argparse
from analyzer.password_analyzer import analyze_password
from analyzer.wordlist_generator import generate_wordlist, save_wordlist

parser = argparse.ArgumentParser()
parser.add_argument('--password', help="Password to check")
parser.add_argument('--inputs', nargs='*', help="Words to build wordlist")

args = parser.parse_args()

if args.password:
    result = analyze_password(args.password)
    print("Password Score:", result["score"])
    print("Guesses:", result["guesses"])
    print("Feedback:", result["feedback"])

if args.inputs:
    words = generate_wordlist(args.inputs)
    save_wordlist(words)
    print("Wordlist saved with", len(words), "words.")
