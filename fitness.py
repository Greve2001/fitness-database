exercisePath = "exercises.txt"
musclePath = "muscles.txt"
relationPath = "exercises_muscles.txt"

def addExercise(name, musclesHit): # str, arr
    # Checks types
    if isinstance(name, str) and isinstance(musclesHit, list):
        pass
    else:
        return print("Wrong input type")
    
    # Create file access
    exc_file = open(exercisePath, "a")
    musc_file = open(musclePath, "r")
    relation_file = open(relationPath, "a+")

    #Check if exercise is already added
    excArr = getFileArr(exercisePath, " ")
    for i in range(len(excArr)):
        if name == excArr[i]:
            return print("Already a exercise of this name")

    #Append exercise
    addDataToFile(exercisePath, name, " ")


    #Find the index for the newly added exercise
    exc_file = open(exercisePath, "a") # Do again to refresh
    excArr = getFileArr(exercisePath, " ") # Get arr with newly added exercise    
    exercise_idx = None
    for i in range(len(excArr)):
        if excArr[i] == name:
            exercise_idx = i
            print("Exercise idx: " + str(exercise_idx))


    # Get indices of all muscles hit
    muscArr = getFileArr(musclePath, " ")
    muscles_indices = []
    for i in range(len(musclesHit)):
        for j in range(len(muscArr)):
            if musclesHit[i] == muscArr[j]:
                muscles_indices.append(j)
    print("Muscles hit indices: " + str(muscles_indices))

    #Append to relation table.
    addDataToFile(relationPath, [exercise_idx, muscles_indices], "?")


def addDataToFile(path, data, seperator):
    f = open(path, "a+") #Append and read
    f.write(str(data) + seperator)
    

def getFileArr(path, seperator):
    file_obj = open(path, "r+") # Read and write
    str = file_obj.read()
    arr = str.split(seperator)
    return arr



addExercise("Squat18", ["Legs", "Hamstrings"])