#percorso per trovare i file.py = cartella.file import classe
from model.model import Model

model = Model()
model.buildGraph() #richiamo il metodo
print("Num nodi:", model.getNumNodi())
print("Num archi:", model.getNumArchi())

f = Fermata(2, "Abbesses", 2.33855,	48.8843)
nodesBFS = model.getBFSNodesFromEdges(f)
# for n in nodesBFS:
#     print(n)