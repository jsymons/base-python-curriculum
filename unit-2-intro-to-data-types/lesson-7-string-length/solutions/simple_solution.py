language = "Python"
name = "Guido Van Rossum"

string_template = "{name} is the creator of {language}"
text = string_template.format(name=name, language=language)

length_of_language = len(language)
length_of_name = len(name)
length_of_text = len(text)
