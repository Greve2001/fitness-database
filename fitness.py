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
    print(relationsArr)
    muscle_idx = getIndexOf(muscle, musclePath, " ")

    exercisesUsingMuscle = []
    for muscle in range(len(relationsArr)):
        print(len(relationsArr[muscle]))
        for i in range(len(relationsArr[muscle])):
            if relationsArr[1][i] == muscle_idx:
                exercise_idx = relationsArr[0]
                exercisesUsingMuscle.append(getNameByIndex(exercise_idx))
    print(exercisesUsingMuscle)

    

    

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


# addExercise("Butterfly", ["Chest"])
exercisesForMuscle('Legs')