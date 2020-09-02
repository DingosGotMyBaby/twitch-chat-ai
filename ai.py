from textgenrnn import textgenrnn

chat = textgenrnn()
chat.train_from_file(r"processed/output.txt", num_epochs=1)
chat.generate()

