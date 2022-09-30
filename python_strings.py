# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
my_first_name = 'Mariel'
#   - my_last_name
#       -set this equal to your last name
my_last_name = 'Johnson'
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
my_year_of_birth = 1982
#   - current_year
#       -set this equal to 2022
current_year = 2022





# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - last two letter of your last name (use the -index)
# print (my_first_name)
# print (my_last_name)
# print (my_first_name[0])
# print (my_last_name[-6])
# print (my_first_name[0:2])
# print (my_last_name[-2:])



#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times
# print (my_first_name,my_last_name)
# print ((my_first_name +"\n") * 6)



# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - Birth Year Statement first name last name -was born in- year of birth
#       - Current Year Statement first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
# birth_year_statement = my_first_name + my_last_name + 'was born in' + str(my_year_of_birth)
# print(birth_year_statement)

birth_year_statement = "{} {} was born in {}"
print(birth_year_statement.format(my_first_name, my_last_name, my_year_of_birth))

current_year_statement = "{} {} was born in {}. {} enjoyed celebrating {}."
print(current_year_statement.format(my_first_name,my_last_name,my_year_of_birth,my_first_name,current_year))

# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year


# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case