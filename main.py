from pets import Dog, Cat

def main():
  shelter = [Dog("Bantay", 3), Cat("Mingming", 2)]

  for pet in shelter:
    print(pet.describe())
    print(pet.play())
    print("---")
    
if __name__ == "__main__":
main()
