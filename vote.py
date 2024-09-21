def check_voter_age(age):
    if age < 18 :
        raise ValueError("Sorry, you are not eligible to vote.")
    elif age > 100:
        raise ValueError("age must be between 18 to 100")
        
    else:
        print("Congratulations! You are eligible to vote.")


def main():
    try:
        age = int(input("Enter your age : "))
        check_voter_age(age)
    except ValueError as ve:
        print("Invalid input:Please enter a valid age.")
        print("Error message:", ve)
    


if __name__ == "__main__":
    main()
