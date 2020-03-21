

# Render the canvas
def print_canvas(row, col) : 
      
    for i in range(1, row+1) : 
        for j in range(1, col+1) : 
            if (i == 1 or i == row or
                j == 1 or j == col) : 
                print("*", end="")             
            else : 
                print(" ", end="")             
          
        print() 

print_canvas(5, 10)


# # Have the user choose the dimensions of the canvas
# row = int(input("Enter the Total Number of Rows  : "))
# col = int(input("Enter the Total Number of Columns  : "))

