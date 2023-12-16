#!/usr/bin/env python

import argparse
from random import randint, seed
from os.path import join

ADJECTIVES = ["afraid", "all", "angry", "beige", "big", "better", "bitter", "blue", "brave", "breezy", "bright", "brown", "bumpy", "busy", "calm", "chatty", "chilly", "chubby", "clean", "clear", "clever", "cold", "crazy", "cruel", "cuddly", "curly", "curvy", "cute", "common", "cold", "cool", "cyan", "dark", "deep", "dirty", "dry", "dull", "eager", "early", "easy", "eight", "eighty", "eleven", "empty", "every", "evil", "fair", "famous", "fast", "fancy", "few", "fine", "fifty", "five", "flat", "fluffy", "floppy", "forty", "four", "free", "fresh", "fruity", "full", "funny", "fuzzy", "gentle", "giant", "gold", "good", "great", "green", "grumpy", "happy", "heavy", "hip", "honest", "hot", "huge", "hungry", "icy", "itchy", "khaki", "kind", "large", "late", "lazy", "lemon", "legal", "light", "little", "long", "loose", "loud", "lovely", "lucky", "major", "many", "mean", "metal", "mighty", "modern", "moody", "nasty", "neat", "new", "nice", "nine", "ninety", "odd", "old", "olive", "open", "orange", "pink", "plain", "plenty", "polite", "poor", "pretty", "proud", "public", "puny", "petite", "purple", "quick", "quiet", "rare", "real", "ready", "red", "rich", "ripe", "rotten", "rude", "sad", "salty", "seven", "shaggy", "shaky", "sharp", "shiny", "short", "shy", "silent", "silly", "silver", "six", "sixty", "slick", "slimy", "slow", "small", "smart", "smooth", "social", "soft", "solid", "some", "sour", "spicy", "spotty", "stale", "strong", "stupid", "sweet", "swift", "tall", "tame", "tangy", "tasty", "ten", "tender", "thick", "thin", "thirty", "three", "tidy", "tiny", "tired", "tough", "tricky", "true", "twelve", "twenty", "two", "upset", "vast", "violet", "warm", "weak", "wet", "whole", "wicked", "wide", "wild", "wise", "witty", "yellow", "young", "yummy"]

NOUNS = ["apes", "animals", "areas", "bars", "banks", "baths", "breads", "bushes", "cloths", "clowns", "clubs", "hoops", "loops", "memes", "papers", "parks", "paths", "showers", "sides", "signs", "sites", "streets", "teeth", "tires", "webs", "actors", "ads", "adults", "aliens", "ants", "apples", "baboons", "badgers", "bags", "bananas", "bats", "beans", "bears", "beds", "beers", "bees", "berries", "bikes", "birds", "boats", "bobcats", "books", "bottles", "boxes", "brooms", "buckets", "bugs", "buses", "buttons", "camels", "cases", "cameras", "candies", "candles", "carpets", "carrots", "carrots", "cars", "cats", "chairs", "chefs", "chicken", "clocks", "clouds", "coats", "cobras", "coins", "corners", "colts", "comics", "cooks", "cougars", "regions", "results", "cows", "crabs", "crabs", "crews", "cups", "cities", "cycles", "dancers", "days", "deer", "dingos", "dodos", "dogs", "dolls", "donkeys", "donuts", "doodles", "doors", "dots", "dragons", "drinks", "dryers", "ducks", "ducks", "eagles", "ears", "eels", "eggs", "ends", "mammals", "emus", "experts", "eyes", "facts", "falcons", "fans", "feet", "files", "flies", "flowers", "forks", "foxes", "friends", "frogs", "games", "garlics", "geckos", "geese", "ghosts", "ghosts", "gifts", "glasses", "goats", "grapes", "groups", "guests", "hairs", "hands", "hats", "heads", "hornets", "horses", "hotels", "hounds", "houses", "humans", "icons", "ideas", "impalas", "insects", "islands", "items", "jars", "jeans", "jobs", "jokes", "keys", "kids", "kings", "kiwis", "knives", "lamps", "lands", "laws", "lemons", "lies", "lights", "lines", "lions", "lizards", "llamas", "mails", "mangos", "maps", "masks", "meals", "melons", "mice", "mirrors", "moments", "moles", "monkeys", "months", "moons", "moose", "mugs", "nails", "needles", "news", "nights", "numbers", "olives", "onions", "oranges", "otters", "owls", "pandas", "pans", "pants", "papayas", "parents", "parts", "parrots", "paws", "peaches", "pears", "peas", "pens", "pets", "phones", "pianos", "pigs", "pillows", "places", "planes", "planets", "plants", "plums", "poems", "poets", "points", "pots", "pugs", "pumas", "queens", "rabbits", "radios", "rats", "ravens", "readers", "rice", "rings", "rivers", "rockets", "rocks", "rooms", "roses", "rules", "schools", "bats", "seals", "seas", "sheep", "shirts", "shoes", "shrimps", "singers", "sloths", "snails", "snakes", "socks", "spiders", "spies", "spoons", "squids", "stars", "states", "steaks", "wings", "suits", "suns", "swans", "symbols", "tables", "taxes", "taxis", "teams", "terms", "things", "ties", "tigers", "times", "tips", "toes", "towns", "tools", "toys", "trains", "trams", "trees", "turkeys", "turtles", "vans", "views", "walls", "walls", "wasps", "waves", "ways", "weeks", "windows", "wolves", "women", "wombats", "words", "worlds", "worms", "yaks", "years", "zebras", "zoos"]

VERBS = ["accept", "act", "add", "admire", "agree", "allow", "appear", "argue", "arrive", "ask", "attack", "attend", "bake", "bathe", "battle", "beam", "beg", "begin", "behave", "bet", "boil", "bow", "brake", "brush", "build", "burn", "buy", "call", "camp", "care", "carry", "change", "cheat", "check", "cheer", "chew", "clap", "clean", "cough", "count", "cover", "crash", "create", "cross", "cry", "cut", "dance", "decide", "deny", "design", "dig", "divide", "do", "double", "doubt", "draw", "dream", "dress", "drive", "drop", "drum", "eat", "end", "enter", "enjoy", "exist", "fail", "fall", "feel", "fetch", "film", "find", "fix", "flash", "float", "flow", "fly", "fold", "follow", "fry", "give", "glow", "go", "grab", "greet", "grin", "grow", "guess", "hammer", "hang", "happen", "heal", "hear", "help", "hide", "hope", "hug", "hunt", "invent", "invite", "itch", "jam", "jog", "join", "joke", "judge", "juggle", "jump", "kick", "kiss", "kneel", "knock", "know", "laugh", "lay", "lead", "learn", "leave", "lick", "like", "lie", "listen", "live", "look", "lose", "love", "make", "march", "marry", "mate", "matter", "melt", "mix", "move", "nail", "notice", "obey", "occur", "open", "own", "pay", "peel", "play", "poke", "post", "press", "prove", "pull", "pump", "pick", "punch", "push", "raise", "read", "refuse", "relate", "relax", "remain", "repair", "repeat", "reply", "report", "rescue", "rest", "retire", "return", "rhyme", "ring", "roll", "rule", "run", "rush", "say", "scream", "see", "search", "sell", "send", "serve", "shake", "share", "shave", "shine", "show", "shop", "shout", "sin", "sink", "sing", "sip", "sit", "sleep", "slide", "smash", "smell", "smile", "smoke", "sneeze", "sniff", "sort", "speak", "spend", "stand", "start", "stay", "stick", "stop", "stare", "study", "suffer", "swim", "switch", "take", "talk", "tan", "tap", "taste", "teach", "tease", "tell", "thank", "think", "throw", "tickle", "tie", "trade", "train", "travel", "try", "turn", "type", "unite", "vanish", "visit", "wait", "walk", "warn", "wash", "watch", "wave", "wear", "win", "wink", "wish", "wonder", "work", "worry", "write", "yawn", "yell"]

def random_item(src: list[str]) -> str:
    return src[randint(0, len(src) - 1)]

def dump_strings(count: int, dir: str):
    with open(join(dir, "string-dataset.txt"), "w") as file:
        for _ in range(count):
            adjective = random_item(ADJECTIVES)
            noun = random_item(NOUNS)
            verb = random_item(VERBS)

            concat = "{}{}{}\n".format(adjective.title(), noun.title(), verb.title())
            file.write(concat)

def dump_integers(count: int, dir: str):
    with open(join(dir, "integer-dataset.txt"), "w") as file:
        NORMAL = 2_000_000
        for _ in range(count):
            file.write("{}\n".format(randint(-NORMAL, NORMAL)))

def main():
    seed(0) # ensure deterministic
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int)
    parser.add_argument("-o", "--output-dir", type=str)
    parser.add_argument("-i", "--integer-dataset", action="store_true")
    parser.add_argument("-s", "--string-dataset", action="store_true")

    args = parser.parse_args()

    if args.count == None:
        print("Count not specified, exiting...")
        return

    count = args.count
    output_dir = args.output_dir or ""

    if args.string_dataset:
        dump_strings(count, output_dir)
    if args.integer_dataset:
        dump_integers(count, output_dir)

if __name__ == "__main__":
    main()
