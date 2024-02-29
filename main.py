def is_a_valid_assignment(current_giver, receiver, couples, people_with_gift, matches):
    #
    #   Utility function that defined if a match is valid or not
    #

    # We check if the giver and receiver is not a couple
    for name1, name2 in couples:
        if name1 == current_giver and name2 == receiver:
            return False
        elif name2 == current_giver and name1 == receiver:
            return False
    
    # We check if the receiver is not already giving to the giver
    for match_giver, match_receiver in matches.items():
        if receiver == match_giver and current_giver == match_receiver:
            return False

    return (receiver not in people_with_gift) and (receiver != current_giver)

def get_santas(names_list, couples, matches={}, current_rep=0, verbose=False):
    #
    #   Main recursion function
    #

    if verbose:
        print(f"called with matches: {matches}")
        print(f"and current rep: {current_rep}")

    # If we are done with the matches we return the result
    if len(names_list) == current_rep:
        return matches
    
    # We extract the current_giver for clarity
    current_giver = names_list[current_rep]
    # And we get the list of people who already received a gift
    people_with_gift = [value for key, value in matches.items()]

    if verbose:
        print(f"Current giver is {current_giver}\n")
    # Then we loop through the list of names to find a potential receiver
    for receiver in names_list:
        if verbose:
            print(f"Trying with receiver {receiver}")
        
        # We check if this receiver is valid based on defined conditions
        if is_a_valid_assignment(current_giver, receiver, couples, people_with_gift, matches):

            if verbose:
                print("Receiver is valid !\n")

            # If the assignment is valid, we update the matches dictionary, and recurse for the next giver
            matches[current_giver] = receiver
            if get_santas(names_list, couples, matches, current_rep + 1, verbose=verbose):
                return matches
            # If there was no possible outcome with this assignment, we forget it, and try the next one
            del matches[current_giver]
    if verbose:
        print()

    return False





import sys

TEST_1 = "exercice"
TEST_2 = "error_samename"
TEST_3 = "nocouples"
TEST_4 = "morenames"
TEST_5 = "error_few"
TEST_6 = "few"

if __name__ == '__main__':
    arguments = sys.argv

    verbose = ("-v" in arguments)

    if len(arguments) > 1:
        if arguments[1] == TEST_1:
            # EXERCICE EXAMPLE
            PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
            COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]
            matches = get_santas(PEOPLE, COUPLES, verbose=verbose)
        elif arguments[1] == TEST_2:
            # ERROR BECAUSE 2 TIMES THE SAME NAME
            PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien", "Bastien"]
            COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]
            matches = get_santas(PEOPLE, COUPLES, verbose=verbose)
        elif arguments[1] == TEST_3:
            # TEST WITHOUT ANY COUPLES
            PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
            COUPLES = []
            matches = get_santas(PEOPLE, COUPLES, verbose=verbose)
        elif arguments[1] == TEST_4:
            # TEST WITH MORE NAMES AND SAME COUPLES
            PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien", "Arnaud", "Romain", "Roman", "Lea"]
            COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]
            matches = get_santas(PEOPLE, COUPLES, verbose=verbose)
        elif arguments[1] == TEST_5:
            # ERROR BECAUSE 3 NAMES AND A COUPLE
            PEOPLE = ["Florent", "Jessica", "Coline",]
            COUPLES = [("Florent", "Jessica")]
            matches = get_santas(PEOPLE, COUPLES, verbose=verbose)
        elif arguments[1] == TEST_6:
            # TEST WITH 4 NAMES AND A COUPLE
            PEOPLE = ["Florent", "Jessica", "Coline", "Arnaud"]
            COUPLES = [("Florent", "Jessica")]
            matches = get_santas(PEOPLE, COUPLES, verbose=verbose)
    else:
        # EXERCICE EXAMPLE
        PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
        COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]
        matches = get_santas(PEOPLE, COUPLES, verbose=verbose)

    if not matches:
        print("It is impossible to assign using my rules.")
    else:
        print(f"Here are your assignments: {matches}")
