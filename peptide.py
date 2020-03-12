import requests
import urllib
import json

sequence=input('What is your peptide sequence?')
Nterm=input('What is your N-terminal modification?')
Cterm=input('What is your C-terminal modification?')


def peptideBasics(sequence, Nterm, Cterm):

  resp = requests.get("http://api.pep-calc.com/peptide?seq=" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  #resp = requests.get("http://api.pep-calc.com/" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  #resp2 = requests.get("http://api.pep-calc.com/peptide/betacontiguity?seq=" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  print(resp)
  data = resp.json()
  return data



data = peptideBasics(sequence, Nterm, Cterm)
print(data)