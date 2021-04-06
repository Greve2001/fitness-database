import ast

exercisePath = "exercises.txt"
musclePath = "muscles.txt"
relationPath = "exercises_muscles.txt"

exerciseFile = None
musc_file = None
relation_file = None 

def addExercise(name, musclesHit): # str, arr
    # Checks types
    if isinstance(name, str) and isinstance(musclesHit, list):
        pass
    else:
        return print("Wrong input type")
    
    # Create file access
    createFileAccess()
    
    #Check if exercise is already added
    exerciseArr = getFileArr(exercisePath, " ")
    for i in range(len(exerciseArr)):
        if name == exerciseArr[i]:
            return print("Already a exercise of this name")

    #Append exercise
    addDataToFile(exercisePath, name, " ")

    createFileAccess() # Refresh to update file    
    exercise_idx = getIndexOf(name, exercisePath, " ")
    muscles_indices = getIndicesOf(musclesHit, musclePath, " ")

    #Append to relation table.
    addDataToFile(relationPath, [exercise_idx, muscles_indices], "?")

def exercisesForMuscle(muscle): #Takes a muscle and shows what exercises contain this muscle
    createFileAccess()
    relationsArr = getFileArr(relationPath, "?")
    relationsArrEvaluated = evaluateArray(relationsArr)

    muscle_idx = getIndexOf(muscle, musclePath, " ")

    exercisesUsingMuscle = []
    for relation in range(len(relationsArrEvaluated)):
        for muscleUsed in range(len(relationsArrEvaluated[relation][1])):
            if relationsArrEvaluated[relation][1][muscleUsed] == muscle_idx:
                exerciseName = getNameByIndex(relationsArrEvaluated[relation][0], exercisePath, " ")
                exercisesUsingMuscle.append(exerciseName)
    print("Exercises using " + str(muscle) + ": " + str(exercisesUsingMuscle))
        
def musclesUsedInExercise(exercise):
    createFileAccess()
    relationsArr = getFileArr(relationPath, "?")
    relationsArrEvaluated = evaluateArray(relationsArr)

    exercise_idx = getIndexOf(exercise, exercisePath, " ")
    musclesUsed = []
    for relation in range(len(relationsArrEvaluated)):
        if relationsArrEvaluated[relation][0] == exercise_idx:
            for muscle in range(len(relationsArrEvaluated[relation][1])):
                muscleName = getNameByIndex(relationsArrEvaluated[relation][1][muscle], musclePath, " ")
                musclesUsed.append(muscleName)
    print("You use " + str(musclesUsed) + " to perform " + str(exercise))

def addDataToFile(path, data, seperator):
    f = open(path, "a+") #Append and read
    f.write(str(data) + seperator)
    print("Added " + str(data) + " to file: " + str(path))

def getFileArr(path, seperator):
    file_obj = open(path, "r+") # Read and write
    str = file_obj.read()
    arr = str.split(seperator)
    return arr

def getIndexOf(value, path, seperator):
    arr = getFileArr(path, seperator=" ") # Get arr with newly added exercise
    if isinstance(value, str): # Single value
        for i in range(len(arr)):
            if arr[i] == value:
                idx = i
        return idx
    else:
        print("Error")
def getIndicesOf(arr, path, seperator): # The path gets used to find an array.
    pathArr = getFileArr(path, " ")
    if isinstance(arr, list): 
        indices = []
        for i in range(len(arr)):
            for j in range(len(pathArr)):
                if arr[i] == pathArr[j]:
                    indices.append(j)
        return indices
    else:
        print("Error")

def getNameByIndex(idx, path, seperator):
    arr = getFileArr(path, seperator)
    return arr[idx]

def createFileAccess():
    exerciseFile = open(exercisePath, "a")
    musc_file = open(musclePath, "r")
    relation_file = open(relationPath, "a+")

def evaluateArray(array):
    newArr = []
    for i in range(len(array)):
        try:
            e = ast.literal_eval(array[i])
            newArr.append(e)
        except:
            pass # Will catch the empty string
    return newArr    
        
# addExercise("Deadlift", ["Legs", "Hamstrings", "Back"])
# exercisesForMuscle('Back')
musclesUsedInExercise("Deadlift")