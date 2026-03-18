class Student:
    def __init__(self, name, num_scores):
        self.name = name
        self.test_scores = [0] * num_scores

    def getName(self):
        return self.name

    def getScore(self, position):
        return self.test_scores[position]

    def setScore(self, position, value):
        self.test_scores[position] = value

    def getHighestScore(self):
        return max(self.test_scores)

    def getAverageScore(self):
        return sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        return f"Student: {self.name}, Scores: {self.test_scores}"
