import pickle
from datetime import datetime

jimi = datetime(1969, 8, 18, hour=9)  # koncert Jimiego Hendrixa na festiwalu Woodstock

print(jimi)

dane_json = pickle.dumps(jimi)  # Niestety, tylko podstawowe typy są serializowalne do formatu JSON

print(dane_json)

