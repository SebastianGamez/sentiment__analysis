from pysentimiento import create_analyzer
analyzer = create_analyzer(task="sentiment", lang="es")

print(analyzer.predict("Peña no debe ser el rector de la Universidad Nacional de Colombia. Su proceso de elección fue ciertamente democratico; sin embargo, en este no participan los estudiantes").probas)
