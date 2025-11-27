


def split_before_uppercases(formula):
    """
    Splits a chemical formula into chunks whenever an uppercase letter appears.
    Examples:
        "H2O" -> ["H2", "O"]
        "MgCl2" -> ["Mg", "Cl2"]
    """
    parts = []
    current = ""

    for char in formula:
        # If we see an uppercase letter, this means a new element starts
        if char.isupper():
            # Save previous element
            if current: # if currnt == "" return False
                parts.append(current)
            # Start new element
            current = char
        else:
            current += char # currnt = current + char

    # Add last collected part
    if current: # if currnt == "" return False
        parts.append(current)

    return parts

def split_at_digit(formula):
    """
    Splits an element string into (element_name, count).
    Examples:
        "H2" -> ("H", 2)
        "O"  -> ("O", 1)
        "Cl15" -> ("Cl", 15)
    """

    letters = ""   # will hold the element name (like "H", "Cl")
    digits = ""    # will hold the number (like "2", "15")

    # Go over each character and separate letters from digits
    for char in formula:
        if char.isdigit():
            digits += char
        else:
            letters += char

    # If no digits found → count is 1
    if digits == "":
        count = 1
    else:
        count = int(digits)

    return letters, count




def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        
        # Step 2: Update the dictionary with the atom name and count
        atom_counts[atom_name] = atom_counts.get(atom_name,0) + atom_count
    # Step 3: Return the completed dictionary
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
