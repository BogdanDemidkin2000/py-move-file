import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3 and command_parts[0] == "mv":
        directory, filename = os.path.split(command_parts[2])

        if not directory:
            if os.path.exists(command_parts[1]):
                os.rename(command_parts[1], command_parts[2])
            else:
                return
        else:
            dst_dir = os.path.dirname(command_parts[2])
            if dst_dir and not os.path.isdir(dst_dir):
                os.makedirs(dst_dir, exist_ok=True)

            with open(command_parts[1], "r") as old_file, \
                    open(command_parts[2], "w") as new_file:
                new_file.write(old_file.read())
            os.remove(command_parts[1])
