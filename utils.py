def default_parsing_fn(line):
    return line

def get_file(filename, parsing_fn):
    lines = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            lines.append(parsing_fn(line))
    return lines