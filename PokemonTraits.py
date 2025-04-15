import random

Natures = {
    "Adamant": {
        "Attack": .1,
        "SpAttack": -.1
    },
    "Bashful": {
        "Health": 0,
        "Attack": 0,
        "Defense": 0,
        "SpAttack": 0,
        "SpDefense": 0,
        "Speed": 0
    },
    "Bold": {
        "Defense": .1,
        "Attack": -.1
    },
    "Brave": {
        "Attack": .1,
        "Speed": -.1
    },
    "Calm": {
        "SpDefense": .1,
        "Attack": -.1
    },
    "Careful": {
        "SpDefense": .1,
        "SpAttack": -.1
    },
    "Docile": {
        "Health": 0,
        "Attack": 0,
        "Defense": 0,
        "SpAttack": 0,
        "SpDefense": 0,
        "Speed": 0
    },
    "Gentle": {
        "SpDefense": .1,
        "Defense": -.1
    },
    "Hardy": {
        "Health": 0,
        "Attack": 0,
        "Defense": 0,
        "SpAttack": 0,
        "SpDefense": 0,
        "Speed": 0
    },
    "Hasty": {
        "Speed": .1,
        "Defense": -.1
    },
    "Impish": {
        "Defense": .1,
        "SpAttack": -.1
    },
    "Jolly": {
        "Speed": .1,
        "SpAttack": -.1
    },
    "Lax": {
        "Defense": .1,
        "SpDefense": -.1
    },
    "Lonely": {
        "Attack": .1,
        "Defense": -.1
    },
    "Mild": {
        "SpAttack": .1,
        "Defense": -.1
    },
    "Modest": {
        "SpAttack": .1,
        "Attack": -.1
    },
    "Naive": {
        "Speed": .1,
        "SpDefense": -.1
    },
    "Naughty": {
        "Attack": .1,
        "SpDefense": -.1
    },
    "Quiet": {
        "SpAttack": .1,
        "Speed": -.1
    },
    "Rash": {
        "SpAttack": .1,
        "SpDefense": -.1
    },
    "Relaxed": {
        "Defense": .1,
        "Speed": -.1
    },
    "Sassy": {
        "SpDefense": .1,
        "Speed": -.1
    },
    "Serious": {
        "Health": 0,
        "Attack": 0,
        "Defense": 0,
        "SpAttack": 0,
        "SpDefense": 0,
        "Speed": 0
    },
    "Timid": {
        "Speed": .1,
        "Attack": -.1
    }
}

def GenerateGender(female_ratio,male_ratio):
        total_ratio = female_ratio + male_ratio
        female_probability = female_ratio / total_ratio
        male_probability = male_ratio / total_ratio
        gender = random.choices(["Female", "Male"], weights=[female_probability, male_probability])[0]
        return gender

def GenerateIvs():
        ivs = {
            "Health": random.randint(0, 31),
            "Attack": random.randint(0, 31),
            "Defense": random.randint(0, 31),
            "SpAttack": random.randint(0, 31),
            "SpDefense": random.randint(0, 31),
            "Speed": random.randint(0, 31)
        }
        return ivs

def CreateEvsData():
      return {
            "Health": 0,
            "Attack": 0,
            "Defense": 0,
            "SpAttack": 0,
            "SpDefense": 0,
            "Speed": 0
        }

def GenerateNature():
    return random.choice(list(Natures.keys()))

def GetNatureValues(Nature):
    return Natures.get(Nature)
