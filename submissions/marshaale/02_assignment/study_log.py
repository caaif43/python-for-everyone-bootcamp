def main():
    notes = load_notes("notes.txt")
    print(notes)

def load_notes(path):
    notes = []
    try:
        with open(path,'r',encoding='utf-8') as f:
            lines = f.readlines()
            notes = [x.strip('\n') for x in lines]
    except FileNotFoundError:
        print(f"File {path} does not exists")
    return notes


def save_notes(path,notes):
    pass

if __name__ == "__main__":
    main()
