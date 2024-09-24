def dictionaryMerger(A , B):
    #update method, merge B to A but doesn't return any. O(n)  (A.update(B))
    #

    res = {**A , **B}
    return res


city = {
    'name': 'Galway',
    'country': 'Ireland'
}

capital = {
    'name': 'Dublin',
    'capital': True
}

print(dictionaryMerger(city, capital))