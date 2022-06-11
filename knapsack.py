import numpy as np
class KnapSack:
    '''
    Encapsulates KnapSack problem defined on rosettacode website: http://rosettacode.org/wiki/Knapsack_problem/0-1#C.2B.2B
    '''
    def __init__(self) -> None:
        self.items = []
        self.max_weight = 0
        self.__initItems()
    
    def __initItems(self) -> None:
        '''
        Initializes the items for KnapSack problem with weight and values from http://rosettacode.org/wiki/Knapsack_problem/0-1#C.2B.2B.
        '''
        self.items = [
                    ("map", 9, 150),
                    ("compass", 13, 35),
                    ("water", 153, 200),
                    ("sandwich", 50, 160),
                    ("glucose", 15, 60),
                    ("tin", 68, 45),
                    ("banana", 27, 60),
                    ("apple", 39, 40),
                    ("cheese", 23, 30),
                    ("beer", 52, 10),
                    ("suntan cream", 11, 70),
                    ("camera", 32, 30),
                    ("t-shirt", 24, 15),
                    ("trousers", 48, 10),
                    ("umbrella", 73, 40),
                    ("waterproof trousers", 42, 70),
                    ("waterproof overclothes", 43, 75),
                    ("note-case", 22, 80),
                    ("sunglasses", 7, 20),
                    ("towel", 18, 12),
                    ("socks", 4, 50),
                    ("book", 30, 10)
                    ]
        self.max_weight = 400

    def getValue(self, binarylist: list) -> int:
        '''
        Calculates the total value of items in the binarylist, while ignoring items that causes total weight to exceed maximun capacity of KnapSack.
        :param binarylist: list of items to be added to KnapSack 1: item is added, 0: item is not added.
        :return: total value
        '''
        total_weight = 0
        total_value = 0
        for i,item in enumerate(self.items):
            weight, value = item[1:]
            if total_weight + weight <= self.max_weight:
                total_weight += binarylist[i] * weight
                total_value += binarylist[i] * value
        return total_value
    
    def printItems(self, binarylist: list) -> None:
        """
        Prints the selected items in the binarylist, while ignoring items that causes total weight to exceed maximun capacity of KnapSack.
        :param binarylist: list of items to be added to KnapSack 1: item is added, 0: item is not added.
        """
        total_weight = 0
        total_value = 0
        print("---------------------------------------------------------------------------------------")
        print('{0: <22}'.format('Item')+"\t\t\tWeight\tValue\tTweight\tTvalue")
        for i,item in enumerate(self.items):
            weight, value = item[1:]
            if total_weight + weight <= self.max_weight:
                if binarylist[i] ==1:
                    total_weight += weight
                    total_value += value
                    print('{0: <22}'.format(item[0])+ f"\t\t\t{weight}\t{value}\t{total_weight}\t{total_value}")
    
    def __len__(self):
        return len(self.items)

