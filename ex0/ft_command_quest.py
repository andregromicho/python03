import sys


def ft_command_quest() -> None:
    print(f"Program name: {sys.argv[0]}")
    arguments = sys.argv[1:]
    for i in range(len(arguments)):
        print(f"Argument {i + 1}: {arguments[i]}")
    print(f"Total arguments: {len(arguments) + 1}")


if __name__ == "__main__":
    ft_command_quest()
