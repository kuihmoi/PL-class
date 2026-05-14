import traceback
try:
    with open("nofile.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error message: {str(e)}")
    print(f"Error arguments: {e.args}")
    print(f"error number: {e.errno}")
    print(f"stack trace:")
    traceback.print_exc()