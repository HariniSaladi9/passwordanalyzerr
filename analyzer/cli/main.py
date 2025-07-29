import argparse
from analyzer.password_analyzer import analyze_password
from analyzer.wordlist_generator import generate_wordlist, save_wordlist

parser = argparse.ArgumentParser()
parser.add_argument('--password', help="Password to check")
parser.add_argument('--inputs', nargs='*', help="Words to build wordlist")

args = parser.parse_args()

if args.password:
    result = analyze_password(args.password)
    print("Score:", result["score"])
    print("Feedback:", result["feedback"])

if args.inputs:
    words = generate_wordlist(args.inputs)
    save_wordlist(words)
    print("Wordlist saved with", len(words), "words.")
