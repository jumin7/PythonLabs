#Lab 07 Practicing control and exception handling
# Jumin Shrestha
# 26 Oct 2021

cwid= []
test_score=[]

def read_test_result():
    user_cwid = input("Enter the CWID you want to add. (Enter blank line if you want to end): ")
    raw_score = input("Enter the raw score.")
        
    if user_cwid == "" or raw_score == "":
        user_cwid = ""
        raw_score = 0
    else:
      	raw_score = int(raw_score)
    return (user_cwid,raw_score)

def main():
    while True:
        try:
            user_cwid, raw_score = read_test_result()
            if (user_cwid == ""):
              break
            else:
              cwid.append(user_cwid)
              test_score.append(raw_score)
        # Value error if incorrect type of data entered
        except ValueError:
            print ("You entered an invalid entry, please try again")
        
    
    # final display print of the lists
    for i in range(len(cwid)):
     	print(
        cwid[i],
        test_score[i],
    	)

main()