import numpy as np

c = 1

class Perceptron:
    def __init__(self, classes_count, features_count):
        self.__classes_count = classes_count
        self.__features_count = features_count
        self.__weights = np.zeros((classes_count, features_count))

    def learn(self, vector, vector_class):
        right_d_value = np.dot(vector, self.__weights[vector_class])
        incorrect_weights = []

        def count_for_wrong(weight_index):
            d = np.dot(vector, self.__weights[weight_index])
            if not right_d_value > d:
                incorrect_weights.append(weight_index)

        for i in range(vector_class):
            count_for_wrong(i)

        for i in range(vector_class + 1, self.__classes_count):
            count_for_wrong(i)

        wrong = len(incorrect_weights) > 0

        if wrong:
            self.__weights[vector_class] += c * vector
            for i in range(len(incorrect_weights)):
                self.__weights[incorrect_weights[i]] -= c * vector

        return wrong

    def __str__(self):
        func_str = ""
        for i in range(self.__classes_count):
            func_str += f"d{i}(x) = "
            for j in range(self.__features_count):
                func_str += f"{self.__weights[i][j]:+} * x{j + 1} "
            func_str += "\n"
        return func_str