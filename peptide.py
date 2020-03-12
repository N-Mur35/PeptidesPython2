import requests
import urllib
import json

sequence =input('What is your peptide sequence?')
nterm=input('What is your N-terminal modification?')
cterm=input('What is your C-terminal modification?')

def peptideBasics(sequence, Nterm, Cterm):

  resp = requests.get("http://api.pep-calc.com/peptide?seq=" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  #resp = requests.get("http://api.pep-calc.com/" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  #resp2 = requests.get("http://api.pep-calc.com/peptide/betacontiguity?seq=" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  print(resp)
  data = resp.json()
  return data


data = peptideBasics("PSICHVHRPDWPCWYR", 'H', 'OH')
print(data)