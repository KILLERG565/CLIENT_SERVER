import socket

host = "192.168.254.102"
port = 7777

# create client socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive difficulty prompt
difficulty_prompt = s.recv(1024).decode()
print(difficulty_prompt)

# Choose difficulty: 1=Easy (1–10), 2=Medium (1–50), 3=Hard (1–100)
difficulty = 2  # adjust this as needed
s.sendall(f"{difficulty}\n".encode())

# Set range based on difficulty
if difficulty == 1:
    low, high = 1, 10
elif difficulty == 2:
    low, high = 1, 50
else:
    low, high = 1, 100

# First game prompt (like "enter guess:")
game_prompt = s.recv(1024).decode()
print(game_prompt)

while True:
    # Calculate guess using binary search
    guess = (low + high) // 2
    print(f"Bot guesses: {guess}")
    s.sendall(f"{guess}\n".encode())

    # Receive server feedback (guess result + new prompt)
    feedback = s.recv(1024).decode()
    print(feedback)

    if "CORRECT" in feedback:
        break
    elif "Lower" in feedback:
        high = guess - 1
    elif "Higher" in feedback:
        low = guess + 1

s.close()
