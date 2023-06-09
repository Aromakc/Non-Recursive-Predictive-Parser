from pprint import pprint
from utils import *
from first import first
from follow import follow
from ll1 import generate_parse_table, parse
from texttable import Texttable

DEBUG_MODE = False

if __name__ == "__main__":

    file_path, test_str = getUserInput(DEBUG_MODE) # Get the file path and test string from the user
    grammar,  grammar_first, grammar_follow = readFile(file_path)

    print("Grammar\n")
    show_dict(grammar)

    for lhs in grammar:
        if(grammar_first[lhs] == "null"):
            grammar_first = first(lhs, grammar, grammar_first)
            
    print("\nFirst\n")
    show_dict(grammar_first) # Show the first set of the grammar


    start = list(grammar.keys())[0] # Get the start symbol of the grammar
    for lhs in grammar: # For each non-terminal symbol A, add $ to Follow(A)
        if(grammar_follow[lhs] == "null"):
            grammar_follow = follow(lhs, grammar, grammar_follow, start, grammar_first)
            
    print("\nFollow\n")
    show_dict(grammar_follow) # Show the follow set of the grammar

    
    non_terminals = generateNonTerminals(grammar) 
    terminals = generateTerminals(grammar)

    parse_table = generate_parse_table(terminals, non_terminals, grammar, grammar_first, grammar_follow)
    display_parse_table(parse_table, terminals, non_terminals)


    expr = test_str

    is_parsed = parse(expr, parse_table, terminals, non_terminals)
    print_result(is_parsed, test_str) 
