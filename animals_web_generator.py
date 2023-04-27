"""My Animal Repository is a python script that generates website
    for animals information from animals API based on user input name."""
from data_fetcher import fetch_data

TEMPLATE_FILE_PATH = "animals_template.html"
HTML_FILE_PATH = "animals.html"


def serialize_animal(animal):
    """Serialize single animal data as html content."""
    li_styles = 'style="padding-top:0.8em"'
    return ('<li class="cards__item">\n'
            '<div class="card__title">'
            f"{animal.get('name').replace('’', '&apos;')}"
            '</div>\n'
            '<p class="card__text">\n'
            '<ul style="list-style-type:none; padding:0;">\n'
            f"{'<li><strong>Class:</strong> ' + animal['taxonomy'].get('class') if 'class' in animal['taxonomy'] else ''}"
            f"{'<li ' + li_styles + '><strong>Diet:</strong> ' + animal['characteristics'].get('diet') if 'diet' in animal['characteristics'] else ''}\n"
            f"{'<li ' + li_styles + '><strong>Location:</strong> ' + animal.get('locations')[0] if 'locations' in animal else ''}\n"
            f"{'<li ' + li_styles + '><strong>Type:</strong> ' + animal['characteristics'].get('type') if 'type' in animal['characteristics'] else ''}"
            f"{'<li ' + li_styles + '><strong>Skin Type:</strong> ' + animal['characteristics'].get('skin_type') if 'skin_type' in animal['characteristics'] else ''}"
            '</p>\n'
            '</ul>\n'
            '</li>')


def get_animals_info(animals):
    """Get animals information from animals API by name from user input.
        Get only fields that exists.
        Serialized animals data as html content."""
    return "\n\n".join([serialize_animal(animal)
                        for animal in animals])


def read_html_data(file_path, animals_by_name):
    """Read html file from template."""
    with open(file_path, "r", encoding='utf-8') as html_file:
        return html_file.read().replace("__REPLACE_ANIMALS_INFO__", animals_by_name)


def write_html_data(file_path, animals_by_name):
    """Create a new html file with the serialized animals data."""
    with open(file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(animals_by_name)


def get_animal_name_from_user():
    """Get user input animal name."""
    animal_name = input("Enter a name of an animal: ")

    while animal_name == '':
        animal_name = input("Enter a name of an animal: ")

    return animal_name.capitalize()


def main():
    """Website generation of animals information from animals API
    based on user input animal name."""
    animal_name = get_animal_name_from_user()
    animals_by_name = fetch_data(animal_name)

    if not animals_by_name:
        html_template_data = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
    else:
        html_template_data = read_html_data(TEMPLATE_FILE_PATH,
                                            get_animals_info(animals_by_name))

    write_html_data(HTML_FILE_PATH, html_template_data)


if __name__ == "__main__":
    main()
