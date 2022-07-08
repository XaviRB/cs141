#Xavier Rodriguez
#Nov 28, 2019
#Description: Gets data from a file and makes the computer determine what is what
###############################################################################
# GLOBAL CONSTANT
# For use as dictionary keys
# You can use this list throughout the program without passing it to a function
# DO NOT MODIFY
ATTRS = []
ATTRS.append("ID")
ATTRS.append("radius")
ATTRS.append("texture")
ATTRS.append("perimeter")
ATTRS.append("area")
ATTRS.append("smoothness")
ATTRS.append("compactness")
ATTRS.append("concavity")
ATTRS.append("concave")
ATTRS.append("symmetry")
ATTRS.append("fractal")
ATTRS.append("class")
###############################################################################


def make_training_set(filename):
    """ Read trainig data from the file whose path is filename.
        Return a list of records, where each record is a dictionary
        containing a value for each of the 12 keys in ATTRS.
    """
    # COMPLETE - DO NOT MODIFY
    training_records = []
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        line_list = line.split(',')
        
        # Create a dictionary for the line and map the attributes in
        # ATTRS to the corresponding values in the line of the file
        record = {}
        
        # read patient ID as an int:
        record[ATTRS[0]] = int(line_list[0].strip())
        
        # read attributes 1 through 10 as floats:
        for i in range(1,11):
            record[ATTRS[i]] = float(line_list[i])
        
        # read the class (label), which is "M", or "B" as a string:
        record[ATTRS[11]] = line_list[31].strip() 

        # Add the dictionary to a list
        training_records.append(record)        

    return training_records


def make_test_set(filename):
    """ Read test data from the file whose path is filename.
        Return a list with the same form as the training
        set, except that each dictionary has an additional
        key "prediction" initialized to "none" that will be
        used to store the label predicted by the classifier. 
    """
    # COMPLETE - DO NOT MODIFY
    test_records = make_training_set(filename)

    for record in test_records:
        record["prediction"] = "none"

    return test_records

def midpoint(x1,x2):
    """This function finds the midpoint by adding the first number
       and the second number then dividing it by 2
       pre-condition is that it needs two inputs
    """
    point = (x1 + x2) / 2 #midpoint formula
    
    return point


def count_malignant(training_records):
    """Counts the malignant times that it shows in training records
        then it gets used in the function to find the midpoint.
        pre-condition: needs to get the training_records so it can read the data off of it.
    """
    #made a counter to count malignant
    count = 0
    #created a for loop checking patient in the records
    for patient in training_records:
        #checks the class and if its M then its counted
        if patient["class"] == 'M':
            #adds one to the counter
            count = 1 + count
                    
    return count

def count_benign(training_records):
    """Counts the benign times that it shows in training records
        then it gets used in the function to find the midpoint.
        pre-condition: needs to get the training_records so it can read the data off of it.
    """
    # made a counter to count benign
    count = 0
    #created a for loop checking patient in the records
    for patient in training_records:
        #checks the class and if its B then its counted
        if patient["class"] == 'B':
            #adds one to the counter
            count = 1 + count
            
    return count

def benign_list(training_records):
    """ This executes the same as count_benign and count_malignant
        but now instead of returning the count it will return a list
        which will help update the list.
    """
    #benign list
    benign = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #created a for loop checking patient in the records
    for patient in training_records:
        #checks the class and if its b if so then it will execute the for loop
        if patient["class"] == 'B':
            index = 0
            # made a for loop in ATTRS 1-11 going through each one helping make a new list
            for benign_new in ATTRS[1:11]:
                #fills in the list 
                benign[index] = patient[benign_new] + benign[index] 
                index = index + 1
    #returns new list            
    return benign

def malignaint_list(training_records):
    """
    """
    #malignant list
    malignant = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #created a for loop checking patient in the records
    for patient in training_records:
        # checks the class and if its M if so then it will execute the for loop
        if patient["class"] == 'M':
            index = 0
            # made a for loop in ATTRS 1-11 going through each one helping make a new list
            for mal_new in ATTRS[1:11]:
                #fills in the list
                malignant[index] = patient[mal_new] + malignant[index] 
                index = 1 + index    
    #returns new list
    return malignant    
    
def train_classifier(training_records):
    """ Return a dict containing the midpoint between averages
        among each class (malignant and benign) of each attribute.
        (See the A5 writeup for a more complete description)
        Precondition: training_records is a list of patient record
                      dictionaries, each of which has the keys
                      in the global variable ATTRS
        Postcondition: the returned dict has midpoint values calculated
                       from the training set for all 10 attributes except
                       "ID" and"class".
    """
    # TODO 1 - implement this function:
    malignant = malignaint_list(training_records)
    benign = benign_list(training_records)
    # the this is just setting up a blank dict so it can be filled in later and will be compared to the classifier 
    compared_list ={"radius":0 , "texture" :0 , "perimeter":0 , "area":0, "smoothness":0 , "compactness":0 , "concavity":0 , "concave":0 , "symmetry":0, "fractal":0}
  
  # average and midpoint will be calculated through range of 0 to 10 doing this 10 times
    for mal_ben_average_midpoint in range (0, 10):
        #finds the benign average 
        average_ben = benign[mal_ben_average_midpoint] / count_benign(training_records)
        #finds the malignant average
        average_mal = malignant[mal_ben_average_midpoint] / count_malignant(training_records)  
        #finds the midpoint between the averages of malignant and benign
        midpoints_both = midpoint(average_ben, average_mal)
        #dic getting filled in
        compared_list[ATTRS[1 + mal_ben_average_midpoint]] = midpoints_both
        
    return compared_list 
    
def classify(test_records, classifier):
    """ Use the given classifier to make a prediction for each record in
        test_records, a list of dictionary patient records with the keys in
        the global variable ATTRS. A record is classified as malignant
        if at least 5 of the attribute values are above the classifier's
        threshold.
        Precondition: classifier is a dict with midpoint values for all
                      keys in ATTRS except "ID" and "class"
        Postcondition: each record in test_records has the "prediction" key
                       filled in with the predicted class, either "M" or "B"
    """
    # TODO 2 - implement this function
    for patient in test_records:
        Malignant = 0 
        Benign = 0 
        #making a for loop saying records in the ATTRS between 1:11
        for records in ATTRS[1:11]:
            #if its in patient checking if the attributes are less then the classifer then depending on that it will either be benign or malignant
            if patient[records] <= classifier[records]: 
                Benign = 1 + Benign
            else:
                Malignant = 1 + Malignant
        #making an if statement that if the votes for m are greater than b then it will be malignant   
        if Malignant >= Benign:
            
            patient["prediction"] = "M" 
        #making it if its less the m then it will just be benign
        else:
            
            patient["prediction"] = "B"

def report_accuracy(test_records):
    """ Print the accuracy of the predictions made by the classifier
        on the test set as a percentage of correct predictions.
        Precondition: each record in the test set has a "prediction"
        key that maps to the predicted class label ("M" or "B"), as well
        as a "class" key that maps to the true class label.
    """
    # TODO 3 - implement this function
    # making a counter for the predictions made and for the ones that are correct
    total = 0
    correct = 0
    #creates records and checks it with the data in test records
    for record in test_records:
        if record["prediction"] == record["class"]: #checks the class if its equal with the predictions
            correct = correct + 1                              # if so then add one the count correct
        #adds one to total
        total = total + 1
    
    accuracy = (correct / total) * (100) #the math for getting the accuracy
    
    print("classifier accuracy:" , accuracy)

def table(ID, test_records):
    """This creates a table and makes a vote either malignant or benign
        pre-condition: needs to get a id given by the user to find if it
        compares with the test_records.
    """
    # looks in test_records 
    for patient in test_records:
        if ID == str(patient["ID"]):
            #prints out the top of the coloums 
            print("\t Attribute      Patient       Classifier      Vote")
            #creates list and checks it in attrs 1-11            
            for lists in ATTRS[1:11]:
                #checks if its going to be benign or malignant
                if patient[lists] >= classifier[lists]: 
                    picks = "Malignant" # one vote goes to the benign counter
                else:
                    picks = "Benign" # one vote goes to the malignant counter
                #adjustments so it fits in the shell properly                
                print(lists.rjust(17), "{:14f}".format(patient[lists]), "{:13f}".format(classifier[lists]), picks.rjust(10))
            
            # checks if the [prediction] from the data has B if so then it will be benign, if not then it will be malignant                
            if patient["prediction"] == "B":
                patient["prediction"] = "Benign"
            else:
                patient["prediction"] = "Malignant"                    
            #prints out the final prediciton 
            print("Classifier’s diagnosis:",patient["prediction"])
                
            ID = input("Please enter a patient ID to see classification details:")
            
def check_patients(test_records, classifier):
    """ Repeatedly prompt the user for a Patient ID until the user
        enters "quit". For each patient ID entered, search the test
        set for the record with that ID, print a message and prompt
        the user again. If the patient is in the test set, print a
        table: for each attribute, list the name, the patient's value,
        the classifier's midpoint value, and the vote cast by the
        classifier. After the table, output the final prediction made
        by the classifier.
        If the patient ID is not in the test set, print a message and
        repeat the prompt. Assume the user enters an integer or quit
        when prompted for the patient ID.
    """
    # TODO 4 - implement this function
    
    # Pseudocode:
    # prompt user for an ID
    ID = input("Enter a patient ID to see classification details:")
    #created a boolean to help the while statment to break it when its called
    confirmed = False
    quit_choice = False 
     
    # while they didn't input quit it wont come back and break it
    while quit_choice == False:
        for patient in test_records:
            if ID == str(patient["ID"]):
                table(ID, test_records)    
        #checks if quit is inputed             
        if ID == "quit" or ID == "Quit":
            quit_choice = True
                        
        else:#if anything else in inputed then it will return with this
            if confirmed == False:
                print("The patient ID you typed wasn't found")
                
            ID = input("Please enter a patient ID to see classification details:")
        # determine whether the entered patient ID is in the test set
        # if it is,
            # print a table of results (see the handout and sample output)
        # otherwise,
            # print a message saying the patient ID wasn't found

        # prompt the user for anoher ID


if __name__ == "__main__": 
    # Main program - COMPLETE
    # Do not modify except to uncomment each code block as described.
    
    # load the training set
    print("Reading in training data...")
    training_data_file = "cancerTrainingData.txt"
    training_set = make_training_set(training_data_file)
    print("Done reading training data.")
    
    # load the test set 
    print("Reading in test data...")
    test_file = "cancerTestingData.txt"
    test_set = make_test_set(test_file)
    print("Done reading test data.\n")

    # train the classifier: uncomment this block once you've
    # implemented train_classifier
    print("Training classifier..."    )
    classifier = train_classifier(training_set)
    print("Classifier cutoffs:")
    for key in ATTRS[1:11]:
        print("    ", key, ": ", classifier[key], sep="")
    print("Done training classifier.\n")

    # use the classifier to make predictions on the test set:
    # uncomment the following block once you've written classify
    # and report_accuracy
    print("Making predictions and reporting accuracy")
    classify(test_set, classifier)
    report_accuracy(test_set)
    print("Done classifying.\n")

    # prompt the user for patient IDs and provide details on
    # the diagnosis: uncomment this line when you've
    # implemented check_patients
    check_patients(test_set, classifier)