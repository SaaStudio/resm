__author__ = 'SuturkinAA'

class Resources:

    def __init__(self, resourcesCount=3):
        self.none = ' '
        self.res = list(self.none*resourcesCount)

    def allocate(self, name):
        i = 0
        for user in self.res:
            if (user == self.none):
                self.res[i] = name
                return "r"+str(i+1)
            i = i + 1
        return False

    def deallocate(self, item):
        if (item>len(self.res)):
            return False
        if (self.res[item-1] != self.none):
            self.res[item-1] = self.none
            return True
        return False

    #any it is name?
    def deallocateByName(self, name):
        i = 0
        isRemove = False
        for user in self.res:
            if (user == name):
                self.res[i] = self.none
                isRemove = True
            i = i + 1
        return isRemove

    def listResource(self):
        allocated = {}

        i = 0
        for user in self.res:
            if (user != self.none):
                #allocated = allocated + {"r"+str(i+1):user}
                allocated["r"+str(i+1)] = user
            i = i + 1

        deallocated = []

        i = 0
        for user in self.res:
            if (user == self.none):
                deallocated = deallocated + ["r"+str(i+1)]
            i = i + 1

        data = [{"allocated":allocated, "deallocated":deallocated}]
        return data

    def listByName(self, name):
        resources = []

        i = 0
        for user in self.res:
            if (user == name):
                resources = resources + ["r"+str(i+1)]
            i = i + 1

        return resources

    def reset(self):
        #self.res = list(self.none*count)
        i = 0
        for user in self.res:
            self.res[i] = self.none
            i = i + 1

    def show(self):
        print(self.res)
