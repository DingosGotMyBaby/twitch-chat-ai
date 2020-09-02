import os, json, sys, glob, demoji

# Download stuff to strip emojis from text
demoji.download_codes()


# Debug
inputpath = r"./training"
outputpath = r"./output/"

with open("bots.csv", "r") as bots_csv:
    known_bots = bots_csv.read().split("\n")

### Converts the imported json into a format that the ai can use
def convert(message_path):
    # Open JSON file containing downloaded twitch chat
    with open(message_path,  encoding="utf-8") as read_file:
        data = json.load(read_file)

    
    filename = outputpath + data["video"]["user_name"] + \
        " - " + data["video"]["id"] + ".txt"
    f = open(filename, "w", encoding='utf-8')
    print("Now converting: "+ filename,end="\n")

    for i in data["comments"]:
        try:
            b=known_bots.index(i["commenter"]["name"])
        except ValueError:
            filtered = demoji.replace_with_desc(i["message"]["body"],sep = ":")
            if r"@" in filtered:
                continue
            else: 
                f.write (filtered + "\n")
        else: continue

for file in os.listdir(inputpath):
    if file.endswith(".json"):
        convert(os.path.join(inputpath,file))
    else: continue
