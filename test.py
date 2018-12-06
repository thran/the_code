import collections


class PFAElo:
    studentsAbility = {}  # students and their ability parameters
    itemsDifficulty = {}  # items and their difficulty parameters

    answersCorrect = [] # actual answers
    answersProbPFAElo = [] # probabilities of correct answer

    knowledgeSI = collections.defaultdict(dict)  # knowledge of one student of one item
    knowledgeSS = collections.defaultdict(dict)  # knowledge of one student of one skill

    # constructor fills up dictionaries
    def __init__(self, divideDataObj):

        self.o = divideDataObj
        # students parameters are set to 0 as a default
        for s in self.o.students:
            self.studentsAbility[s] = [0, 0]  # first item of list: value of parameter, second item: how many times used
        for i in self.o.items:
            self.itemsDifficulty[i] = [0, 0]

    # calculates the number by which the parameter will be updated
    def priorParamUpdate(self, studentAbil, itemDifficul, correct):
        return correct - 1/(1 + exp(-studentAbil + itemDifficul))

    # updates students and items parameters
    def evaluatePriorParams(self, a, sens1, sens2):
        update = self.priorParamUpdate(self.studentsAbility[a.student][0], self.itemsDifficulty[a.item][0], a.correct)
        self.studentsAbility[a.student][1] += 1
        self.itemsDifficulty[a.item][1] += 1

        sensitivityS = sens1/(1 + sens2 * self.studentsAbility[a.student][1])
        sensitivityI = sens1/(1 + sens2 * self.itemsDifficulty[a.item][1])

        self.studentsAbility[a.student][0] += sensitivityS * update
        self.itemsDifficulty[a.item][0] += sensitivityI * (-update)

    def count(self, knowledge):
        return 1/(1 + exp(-knowledge))

    # update of knowledge parameter
    def knowledgeUpdate(self, knowledge, correct, gama, delta):
        if correct == 1:
            return gama * (correct - self.count(knowledge))
        else:
            return delta * (correct - self.count(knowledge))

    # counts final RMSE of PFAe using knowledge parameters for every student and every item
    def countFinalRMSEKnowledgeSI(self, answers, gama, delta, sens1, sens2):
        for a in answers:
            # count initial knowledge param
            if a.student not in self.knowledgeSI.keys() or a.item not in self.knowledgeSI[a.student].keys():
                self.knowledgeSI[a.student][a.item] = self.studentsAbility[a.student][0] - self.itemsDifficulty[a.item][0]

            self.answersProbPFAElo.append(self.count(self.knowledgeSI[a.student][a.item]))
            self.answersCorrect.append(a.correct)
            # update item difficulty and student ability
            self.evaluatePriorParams(a, sens1, sens2)
            # update knowledge params
            self.knowledgeSI[a.student][a.item] += self.knowledgeUpdate(self.knowledgeSI[a.student][a.item], a.correct, gama, delta)

        self.knowledgeSI.clear()
        return RMSE(self.answersCorrect, self.answersProbPFAElo)

    # counts final RMSE of PFAe using unique knowledge parameters for every student and one of five skills
    def countFinalRMSEKnowledgeSS(self, answers, gama, delta, sens1, sens2):
        for a in answers:
            # count initial knowledge params
            if a.student not in self.knowledgeSS.keys() or a.skill_lvl_1 not in self.knowledgeSS[a.student].keys():
                self.knowledgeSS[a.student][a.skill_lvl_1] = self.studentsAbility[a.student][0]

            self.answersProbPFAElo.append(self.count(self.knowledgeSS[a.student][a.skill_lvl_1]))
            self.answersCorrect.append(a.correct)
            # update item difficulty and student ability
            self.evaluatePriorParams(a, sens1, sens2)
            # update knowledge params
            self.knowledgeSS[a.student][a.skill_lvl_1] += self.knowledgeUpdate(self.knowledgeSS[a.student][a.skill_lvl_1], a.correct, gama, delta)
        self.knowledgeSS.clear()
        return RMSE(self.answersCorrect, self.answersProbPFAElo)

    def clearAll(self):
        for s in self.o.students:
            self.studentsAbility[s] = [0, 0]  # parameter,
        for i in self.o.items:
            self.itemsDifficulty[i] = [0, 0]

        self.knowledgeSI.clear()
        self.knowledgeSS.clear()
        self.clearAnswerLists()

    def clearAnswerLists(self):
        self.answersCorrect.clear()
        self.answersProbPFAElo.clear()

def main():
    divideDataObj = DivideData()
    pfaeInput = int(input('Knowledge parameters: for student item type 1, for student skill type 2:'))

    gamaArray = np.arange(0.0, 0.9, 0.1)
deltaArray = np.arange(0.0, 0.9, 0.1)

PFAEloSystem = PFAElo(divideDataObj)
gamaFinal = 0
deltaFinal = 0
smallestRMSE = 1

for gama in gamaArray:
    for delta in deltaArray:
        if pfaeInput == 1:
            rmse = round(PFAEloSystem.countFinalRMSEKnowledgeSI(divideDataObj.answersTrain, gama, delta, 1.2, 0.01), 4)
        elif pfaeInput == 2:
            rmse = round(PFAEloSystem.countFinalRMSEKnowledgeSS(divideDataObj.answersTrain, gama, delta, 1.2, 0.01), 4)

        if rmse < smallestRMSE:
            smallestRMSE = rmse
            gamaFinal = gama
            deltaFinal = delta
        PFAEloSystem.clearAll()
if pfaeInput == 1:
    PFAEloSystem.countFinalRMSEKnowledgeSI(divideDataObj.answersTest, gamaFinal, deltaFinal, 1.2, 0.01)
    PFAEloSystem.clearAnswerLists()
    resultRMSEtest = PFAEloSystem.countFinalRMSEKnowledgeSI(divideDataObj.answersTest, gamaFinal, deltaFinal, 1.2, 0.01)

    PFAEloSystem.countFinalRMSEKnowledgeSI(divideDataObj.answersTest, gamaFinal, deltaFinal, 1.2, 0.01)
resultRMSEallData = PFAEloSystem.countFinalRMSEKnowledgeSI(divideDataObj.answersTest, gamaFinal, deltaFinal, 1.2, 0.01)

elif pfaeInput == 2:
PFAEloSystem.countFinalRMSEKnowledgeSS(divideDataObj.answersTest, gamaFinal, deltaFinal, 1.2, 0.01)
PFAEloSystem.clearAnswerLists()
resultRMSEtest = PFAEloSystem.countFinalRMSEKnowledgeSS(divideDataObj.answersTest, gamaFinal, deltaFinal, 1.2, 0.01)

PFAEloSystem.countFinalRMSEKnowledgeSS(divideDataObj.answersTest, gamaFinal, deltaFinal, 1.2, 0.01)
resultRMSEallData = PFAEloSystem.countFinalRMSEKnowledgeSS(divideDataObj.answersTest, gamaFinal, deltaFinal, 1.2, 0.01)

print('Final RMSE from test data: ' + str(round(resultRMSEtest, 4)))
print('Final RMSE from all data: ' + str(round(resultRMSEallData, 4)))
print('Final MAE from test data: ' + str(round(MAE(PFAEloSystem.answersCorrect, PFAEloSystem.answersProbPFAElo), 4)))
print('Final AUC from test data: ' + str(roc_auc_score(PFAEloSystem.answersCorrect, PFAEloSystem.answersProbPFAElo)))