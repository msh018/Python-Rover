class BidirectionalStepIterator(object):
    """ Bidirectional Step Iterator made to enable simple direction handling during rover rotation

        Attributes
            Collection -- collection of objects used for iteration
            CollectionLength -- stored length of collection to save on processing during next and previous methods
        
        Methods
            Next -- returns the next object in the list looping to the first if last index is provided
                    takes currentIndex as a parameter -- current index of object to be iterated on from collection list
            Prev -- returns the previous object in the list looping to final if first index is provided
                    takes currentIndex as a parameter -- current index of object to be iterated on from collection list
    """

    def __init__(self, collection):
        self.collection = collection
        self.collectionLength = len (collection) - 1

    def next(self, currentIndex):
        if currentIndex == self.collectionLength:
            result = self.collection[0]
        else:
            result = self.collection[currentIndex + 1] 
        return result

    def prev(self, currentIndex):
        if currentIndex == 0:
            result = self.collection[self.collectionLength]
        else: 
            result = self.collection[currentIndex - 1]
        return result