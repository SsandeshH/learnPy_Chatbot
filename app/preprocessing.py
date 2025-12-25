def clean_text(text):
    lines = text.split("\n")
    cleaned = [
        line for line in lines
        if not line.strip().isdigit()  # page numbers
        and "Python Programming" not in line  # book title
    ]
    return "\n".join(cleaned)

