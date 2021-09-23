def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    text = input("Ingresa una palabra: ")
    print(is_palindrome(text))
    if is_palindrome == True:
        print("Es un palindromo!!")
    elif is_palindrome == False:
        print("No es un palindromo")

if __name__ == '__main__':
    run()