s1 = "Where are my solutions to these exercises?"
s2 = s1.split()
print(s2[-2])

###############

class BetterStrings():
    def __init__(self, string: str) -> None:
        self.string = string

    def replace(self, old:list[str], new:list[str]) -> str:
        newString = self.string
        
        for index, old_string in enumerate(old):
            newString = newString.replace(old_string, new[index])

        return newString


s2 = BetterStrings("It is either easy or impossible")
print(s2.replace(['easy', 'impossible'], ['hard', 'possible']))

#################

the_list = ["Where", "are", "the", "solutions"]
print("*".join(the_list))