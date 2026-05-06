with open("story.txt", "r") as f:
    story = f.read()

target_start = "<"
target_end = ">"
start_index = -1

words = set()

for i, char in enumerate(story):
    if char == target_start:

        start_index = i

    elif char == target_end and start_index != -1:
        word = story[start_index: i+1]
        words.add(word)
        start_index = -1


answers = {}

for word in words:
    answer = input("What would you like to replace " + word + " with? ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
print(story)
