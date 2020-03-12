import requests
import urllib
import json

def peptideBasics(sequence, Nterm, Cterm):

  resp = requests.get("http://api.pep-calc.com/peptide?seq=" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  #resp = requests.get("http://api.pep-calc.com/" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  resp2 = requests.get("http://api.pep-calc.com/peptide/betacontiguity?seq=" + sequence + "&N_term=" + Nterm + "&C_term=" + Cterm + "&mz=")

  print(resp)
  data = resp.json()
  return data


data = peptideBasics("PSICHVHRPDWPCWYR", 'H', 'OH')
print(data)
