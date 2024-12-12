class word:
    def reverse_words(self, string):
        return ' '.join(reversed(string.split()))


print(word().reverse_words('Mohammed Said'))