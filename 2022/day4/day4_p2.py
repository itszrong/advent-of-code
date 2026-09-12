def main():
    with open("day4/data.txt", "r") as f:
        contents = f.read()
    

        lines = contents.splitlines()
        result = 0
        for line in lines:
            x, y = line.split(',')
            x_1, x_2 = x.split('-')
            y_1, y_2 = y.split('-')
            
            x_1, x_2 = int(x_1), int(x_2)
            y_1, y_2 = int(y_1), int(y_2)

            if x_1 == y_1 or x_2 == y_2:
                result += 1
            elif x_1 <= y_1 and x_2 >= y_2:
                result +=1 
            elif y_1 <= x_1 and y_2 >= x_2:
                result += 1
            elif y_1 <= x_1 and x_1 <= y_2:
                result += 1 
            elif y_1 <= x_2 and x_2 <= y_2:
                result += 1 
            elif x_1 <= y_1 and y_1 <= x_2:
                result += 1 
            elif x_1 <= y_2 and y_2 <= x_2:
                result += 1 

        print(result)
        
if __name__ == "__main__":
    main()
