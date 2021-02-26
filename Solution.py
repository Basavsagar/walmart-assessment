from collections import  defaultdict
class StoreCounter:
    def findStoreCount(self,storesLocation):
        result = defaultdict(int)
        if storesLocation is None or len(storesLocation)==0:
            return result

        for store in storesLocation:
            key=(store["x"],store["y"])
            result[key]+=1

        return result
