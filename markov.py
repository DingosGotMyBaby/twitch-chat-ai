import markovify

# Get raw text as string.
with open(r"processed/output.txt",encoding="utf8") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

print("sentence \n")
# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

print("\n short sentence \n")
# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(10))