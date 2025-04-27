def add_numbers(numbers)-> int:
    #This function takes a list of numbers and returns their sum.
  
    total:int = 0
    for number in numbers:
        total += number
    return total

def main():
   
   numbers:list[int] = [4, 6, 7, 8, 11]
   sum_of_numbers:int = add_numbers(numbers)
   print(sum_of_numbers)
   
if __name__ == '__main__':
    main()