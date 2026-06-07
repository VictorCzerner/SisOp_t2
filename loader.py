from instruction import instruction

def load_file(path: str):
    commands = []

    with open(path, "r") as file:
      for line in file:
        line = line.strip()
        if line == "":
            continue

        start = line.index("(") + 1     # position right after the (
        end   = line.index(")")         # position of the )
        inner = line[start:end]         # becomes "A, 3"

        if line.upper().startswith("IN"):
            parts = inner.split(",")
            process_id = parts[0].strip()
            size = int(parts[1].strip())
            commands.append(instruction("IN", process_id, size))
        elif line.upper().startswith("OUT"):
            commands.append(instruction("OUT", inner.strip(), None))

    return commands
