import requests
import urllib
import json
import matplotlib.pyplot as plt
import numpy as np

# Asking the user for the inputs:

sequence=input('What is your peptide sequence?')
Nterm=input('What is your N-terminal modification?')
Cterm=input('What is your C-terminal modification?')

# The functions used in the code:

def peptideBasics(sequence, Nterm, Cterm):
    resp = requests.get("http://api.pep-calc.com/peptide?seq=" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

    print(resp)
    data = resp.json()
    return data

data = peptideBasics(sequence, Nterm, Cterm)
print(data)

def AlaSequencetoString(Ala_Sequence):
    str1 = " "
    return(str1.join(Ala_Sequence))

def peptideAlaBasics(Ala_Sequence, Nterm, Cterm):
    resp = requests.get(
        "http://api.pep-calc.com/peptide?seq=" + Ala_Sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

    print(resp)
    Aladata = resp.json()
    return Aladata

def peptideBetacontinguity(Ala_Sequence, Nterm, Cterm):
    resp = requests.get(
        "http://api.pep-calc.com/peptide/betacontiguity?seq=" + Ala_Sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

    print(resp)
    BetaContiguity = resp.json()
    return BetaContiguity

# The Alanine Scanning code:

seqList = sequence
list_of_sequences = []

for (i, item) in enumerate(seqList):
    Ala_Sequence = new_list = []

    for sub_item in seqList:
        new_list.append(sub_item)

    new_list[i] = 'A'

    print(Ala_Sequence)

    seq = AlaSequencetoString(Ala_Sequence)

    print("Sequence: ", seq)

    al_data = peptideAlaBasics(seq, Nterm, Cterm)

    print(al_data)

    mz = al_data['molecularWeight']

    totalmass = float(mz)

    fragments = []

    for n in range(2, 5):
        fragments.append((totalmass + n) / n)

    print("Mass ion series [2H+, 3H+, 4H+]:", fragments)

    betacontig = peptideBetacontinguity(seq, Nterm, Cterm)

    print(betacontig)

    plt.figure()

    beta = betacontig['betaContiguity']

    if beta is not None:
        labellist = []
        valuelist = []

        for b in beta:
            labellist.append(b[1])
            valuelist.append(float(b[2]))

        plt.plot(valuelist)
        plt.xticks(np.arange(len(beta)), labellist)


        plt.show()

list_of_sequences.append(new_list)


print(list_of_sequences)


#Asking the user to put in three inputs: 1. peptide sequence (a sequence of any length up to 50 amino acids made up of any one of twenty letter code for the amino acids)
#2. N-terminal modification (where this can be any one of five already defined by the calculator: 'H', 'CH3', 'C15H11O2', 'C10H15N2O2S', 'C8H9'
#3. C-terminal modification (where this can be any one of five already defined by the calculator: '

# Alanine Scanning Code to take the 'seqList' (the list of amino acid letters which makes up the input sequence) output of Get-requests and iterate over the sequence as many times as required to replace an A in
# every position of the sequence. (Where the enumerate function has added a counter to the iterable (each letter of the amino acid sequence) in order to allow this.
# This requires creation of an empty list_of_sequences = [] and then the for loop runs through the empty tuples created by enumerate and puts in the sequence into this
# The append function then adds the new_list with the A put in to the empty list_of_sequences. Use of join which turns a list into a string, the string can then go back in to the AlanineBasics function get requests

#Use of def to call any of the functions which puts in three inputs (grouped as peptideBasics) into the API in order to return all of the following outputs for each new Alanine scan sequence:
#{'nModified': True or False that there is an N-terminal modification
#'cModified': True or False that there is a C-terminal mod
# 'molecularWeight': A number corresponding to the mass of the sequence
# 'nString': A string corresponding to the N-terminal mod
# 'seqList': A list format of the peptide sequence e.g. ['P', 'S', 'I', 'C'] * seqList is the list which
# 'cString':  A string corresponding to the C-terminal mod
# 'cName': A name for the cString e.g. 'Acid'
# 'seqString': A string format of the peptide sequence e.g. 'PSICHVHRPDW',
# 'formula': A string format corresponding to the molecular formula of the amino acid sequence e.g. 'C32H40N4O8S' *The number of nitrogens e.g. N40 will be the number to feed into the N15 calculation (needs to be defined below)
# 'seqLength': The total number of amino acid letters in the sequence
# 'nName': A name for the nString e.g. 'Fmoc'}

# # The Mass Ion Series get requests is defined by the following for loop which takes the Molecular Weight generated and calculates the ion series:
# for n in range(2, 5):
#     fragments.append((totalmass + n) / n)

# The Beta contiguity calculator is linked in to a module called 'matplotlib' which can be used for drawing plots. So for every new Ala sequence generated, as it's within the for loop:
# It will take the many beta contig output lists generated for each amino acid residue of the new Ala sequence and then the for loop below will search for the second element of the list (b[1]) and
# the third element of the list which is the contiguity value, turn it from a string into a floating point number using float.
#
# for b in beta:
#     labellist.append(b[1])
#     valuelist.append(float(b[2]))

# This is then plotted in matplotlib. Closing each new plot generated will bring up the next one. You need matplotlib installed as a package on Pycharm for this function to work: try pip install matplotlib
# or pip3 install matplotlib

#  There is an if statement written into the Beta contiguity code as for some sequences entered it is not possible to calculate a
# beta contiguity value and therefore needs to be told as long as beta is not none plot it:
# if beta is not None:
#     labellist = []
#     valuelist = []

# *Still to code in to the programme:*

# -Writing a list/ two separate dictionaries of alternative C-terminal modifications and N-terminal modification, writing them  (Fluorescent dyes) and adding them into the calculation so that if a H or OH is chosen
# it can add these numbers on instead (can be in or out of the alanine loop whichever is fine):
#
# eg. Fluorescein = 332.31
#     Rhodamine = 479.02
#     Dansyl = 269.74

# *Using flask to link our code output to a html webpage??, whether its the graphs matplotlib generates or the mass fragment ion series into either a csv file or a html


# Side note: This is how the initial code was written for generating the Alanine scanning for loop:

# seqList = ['R', 'R', 'R']
#
# list_of_sequences = []
#
# for (i, item) in enumerate(seqList):
#   new_list = []
#   for sub_item in seqList:
#    new_list.append(sub_item)
#
#   new_list[i] = 'A'
#
#   list_of_sequences.append(new_list)
#
# print(list_of_sequences)

# An alternative way to do this would be this (untested):
# for i in range(len(seqList)):
#   item = seqList[i]


#
