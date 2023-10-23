import os


def rename_mult_files():
    i = 0
    path = "C:/Users/shoma/OneDrive/Desktop/Beginner_Files/AIPosts/" #desired directory for filenames you look to change
    for filename in os.listdir(path): 
        my_dest = "article" + str(i) + ".txt" #final name
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest) #rename the file
        i += 1 

if __name__ == '__main__': #function is called upon running the file
    rename_mult_files()