import sys

if len(sys.argv) != 3:
    print("Usage: python config_from_args.py <username> <role>")
else:
    username = sys.argv[1]
    role = sys.argv[2]
    print(f"Welcome, {username}! You are logged in as: {role}")
