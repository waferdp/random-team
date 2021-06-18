class ArgumentReader:

    options = []

    def __init__(self, options):
        self.options = options

    def __findOption(self, choice):
        if choice in self.options:
            return self.options[choice]
        return ''

    def __removeDash(self, text):
        return  text.replace('-', '')

    def __split(self, word): 
        return [char for char in word]  

    def __flatten(self, lists):
        flatList = []
        for subList in lists:
            for item in subList:
                flatList.append(item)
        return flatList

    def readArguments(self, argv):
        arguments = []
        if len(argv) > 0:
            listsOfLetters = list(map(self.__split, (map(self.__removeDash, argv))))
            letters = self.__flatten(listsOfLetters)
            arguments = list(map(self.__findOption, letters))
            while '' in arguments:
                arguments.remove('')
        return arguments

