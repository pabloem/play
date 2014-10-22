class Perceptron(object):
    pass
    def __init__(self,dimension,learning_rate,threshold):
        pass
        self.dim = dimension
        self.rate = learning_rate
        self.threshold = threshold
        self.weights = [threshold]*dimension # Initialize the weights to thres.

    def setDim(self,dim):
        self._dim = dim
    def getDim(self):
        return self._dim

    dim = property(fget=getDim, fset=setDim)

    def predict(self,datum):
        pass
        score = 0
        for i in range(datum):
            score += datum[i]*self.weights[i]
        if score >= self.threshold:
            return 1
        return 0 # If score < threshold

    def adjustWeights(self,result,datum):
        for i in range(datum):
            dW = self.learning_rate*datum[i]*result
            self.weights[i] += dW

    def learn(self,data,results,rounds):
        for i in range(len(data)):
            curDatum = data[i]
            assert len(curDatum) == self.dimension

            curRes = results[i]
            predRes = self.predict(curDatum)
            if predRes != curRes:
                pass # PROBLEM. Gotta adjust weights.
                self.adjustWeights(curRes,curDatum)
        return
