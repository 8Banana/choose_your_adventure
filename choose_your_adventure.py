#!/usr/bin/env python3
import argparse

import yaml


class Adventure:
    def __init__(self, adventure_dict):
        self.adventure = adventure_dict
        self.current = self.adventure["start"]

    def make_choice(self, choice):
        assert choice in self.current["choices"]
        self.current = self.adventure[choice]

    def choose_next(self):
        print(self.current["text"])
        print()
        choices = {}
        if not self.current["choices"]:
            return
        e_choices = enumerate(self.current["choices"].items(), start=1)
        for number, (endpoint, text) in e_choices:
            print("{}: {}".format(number, text))
            choices[number] = endpoint
        try:
            choice = int(input("> "))
        except ValueError:
            self.choose_next()
        else:
            if choice in choices:
                self.make_choice(choices[choice])
            self.choose_next()

    @classmethod
    def from_filename(cls, filename):
        with open(filename) as fobj:
            return cls(yaml.load(fobj))


def main():
    argp = argparse.ArgumentParser("choose_your_adventure")
    argp.add_argument("adventure_file",
                      help="The file to load the adventure from")
    argv = argp.parse_args()
    adventure = Adventure.from_filename(argv.adventure_file)
    adventure.choose_next()

if __name__ == "__main__":
    main()
