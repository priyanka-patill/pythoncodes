try:
    # code that may raise different types of exceptions
  
    y = [1, 2, 3]
    print(y[10])
except (ValueError, IndexError) as e:
    print(f"An error occurred: {e}")
