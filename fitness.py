import ast

exercisePath = "exercises.txt"
musclePath = "muscles.txt"
relationPath = "exercises_muscles.txt"

exerciseFile = None
muscleFile = None
relationFile = None 

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
    createFileAccess() # Refresh file access
    # Make the relations array useable
    relationsArr = getFileArr(relationPath, "?")
    relationsArrEvaluated = evaluateArray(relationsArr)

    muscle_idx = getIndexOf(muscle, musclePath, " ") # Get index of the muscle

    exercisesUsingMuscle = [] # Stores the exercises using the muscle specified
    for relation in range(len(relationsArrEvaluated)): # Runs through all the relations
        for muscleUsed in range(len(relationsArrEvaluated[relation][1])): # Runs through all muscles used in this exercise_muscle relation
            if relationsArrEvaluated[relation][1][muscleUsed] == muscle_idx:
                exercise_idx = relationsArrEvaluated[relation][0] # The index of the exercise
                exerciseName = getNameByIndex(exercise_idx, exercisePath, " ") # Get the name by the exercise index
                exercisesUsingMuscle.append(exerciseName) # Add it to the list of exercises
    print("Exercises using " + str(muscle) + ": " + str(exercisesUsingMuscle))
        
def musclesUsedInExercise(exercise):
    createFileAccess() # Refresh file access
    # Make the relations array useful
    relationsArr = getFileArr(relationPath, "?")
    relationsArrEvaluated = evaluateArray(relationsArr)

    exercise_idx = getIndexOf(exercise, exercisePath, " ") # Get exercise index
    musclesUsed = [] # Stores all muscles used in this exercise
    for relation in range(len(relationsArrEvaluated)): # Runs through each relation
        if relationsArrEvaluated[relation][0] == exercise_idx: # Checks forthe relation where the exercise index matches
            for muscle in range(len(relationsArrEvaluated[relation][1])):
                muscle_idx = relationsArrEvaluated[relation][1][muscle] # Index of the muscle
                muscleName = getNameByIndex(muscle_idx, musclePath, " ") # Gets muscle name by index
                musclesUsed.append(muscleName) # Add to list of muscles used
    print("You use " + str(musclesUsed) + " to perform " + str(exercise))

def addDataToFile(path, data, seperator):
    f = open(path, "a+") #Append and read
    f.write(str(data) + seperator) # Writes data, to the open path, f
    print("Added " + str(data) + " to file: " + str(path))

def getFileArr(path, seperator):
    file_obj = open(path, "r+") # Read and write
    str = file_obj.read() # Read the file as a single string
    arr = str.split(seperator) # Splits the file into an array using the seperator
    return arr

def getIndexOf(value, path, seperator):
    arr = getFileArr(path, seperator=" ") # Get arr with newly added exercise
    if isinstance(value, str): # Checks for single value in form of a string
        for i in range(len(arr)): # Loop through arr
            if arr[i] == value:
                idx = i # Keep index that matches value
        return idx
    else:
        print("Error")
def getIndicesOf(arr, path, seperator): # The path gets used to find an array.
    pathArr = getFileArr(path, " ") # Get patharr
    if isinstance(arr, list): # Check that the input is infact a list
        indices = []
        # Loops through both arrays and checks for matching values.
        for i in range(len(arr)):
            for j in range(len(pathArr)):
                if arr[i] == pathArr[j]:
                    indices.append(j) # Store indcies that have a matching value
        return indices
    else:
        print("Error")

def getNameByIndex(idx, path, seperator):
    arr = getFileArr(path, seperator) # Gets relevant list
    return arr[idx] # Returns the value at the index, therefor the name using this index

def createFileAccess():
    exerciseFile = open(exercisePath, "a")
    muscleFile = open(musclePath, "r")
    relationFile = open(relationPath, "a+")

def evaluateArray(array):
    newArr = []
    for i in range(len(array)):
        try:
            e = ast.literal_eval(array[i]) # Compiles the string and turns it into a list, we can use
            newArr.append(e)
        except:
            pass # Will catch the empty string
    return newArr    
        
# addExercise("Deadlift", ["Legs", "Hamstrings", "Back"])
# exercisesForMuscle('Back')
musclesUsedInExercise("Deadlift")