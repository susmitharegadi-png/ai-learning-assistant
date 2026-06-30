import pandas as pd

data = {
    "text": ["I am confused", "This is boring"],
    "emotion": ["Confused", "Bored"]
}

df = pd.DataFrame(data)

print(df)