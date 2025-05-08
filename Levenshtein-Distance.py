import re

text='''After World War II, the British greatly reduced the use of the full stop and other punctuation points after abbreviations in at least semi-formal writing, while the Americans more readily kept such use until more recently, and still maintain it more than Britons. The classic example, considered by their American counterparts quite curious, was the maintenance of the internal comma in a British organisation of secret agents called the "Special Operations, Executive", "S.O., E", which is not found in histories written after about 1960.
But before that, many Britons were more scrupulous at maintaining the French form. In French, the period only follows an abbreviation if the last letter in the abbreviation is not the last letter of its antecedent: "M." is the abbreviation for "monsieur" while "Mme" is that for "madame". Like many other cross-channel linguistic acquisitions, many Britons readily took this up and followed this rule themselves, while the Americans took a simpler rule and applied it rigorously.
Over the years, however, the lack of convention in some style guides has made it difficult to determine which two-word abbreviations should be abbreviated with periods and which should not. The U.S. media tend to use periods in two-word abbreviations like United States (U.S.), but not personal computer (PC) or television (TV). Many British publications have gradually done away with the use of periods in abbreviations.
Minimization of punctuation in typewritten material became economically desirable in the 1960s and 1970s for the many users of carbon-film ribbons since a period or comma consumed the same length of non-reusable expensive ribbon as did a capital letter.
Widespread use of electronic communication through mobile phones and the Internet during the 1990s allowed for a marked rise in colloquial abbreviation. This was due largely to increasing popularity of textual communication services such as instant- and text messaging. SMS, for instance, supports message lengths of 160 characters at most (using the GSM 03.38 character set). This brevity gave rise to an informal abbreviation scheme sometimes called Textese, with which 10% or more of the words in a typical SMS message are abbreviated. More recently Twitter, a popular social networking service, began driving abbreviation use with 140 character message limits.
'''
text=text.lower()
text = re.sub(r'[!:,()".;\'?]', '', text)
word_list=text.split()
word_list=set(word_list)
print(word_list)


def LevenshteinDistance(w1, w2):
    m = len(w1) + 1
    n = len(w2) + 1

    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        dp[i][0] = i
    for j in range(n):
        dp[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if w1[i - 1] == w2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[-1][-1]

def find_min_distance(sentence, dictionary):
    sentence=sentence.lower()
    sentence = re.sub(r'[!:,()".;\'?]', ' ', sentence)
    sentence_words = sentence.split()
    result_list = []

    for word in sentence_words:
     if word not in dictionary:
        min_distance = float('inf')
        closest_words = []

        for dict_word in dictionary:
            distance = LevenshteinDistance(word, dict_word)
            if distance < min_distance:
                min_distance = distance
                closest_words = [dict_word]
            elif distance == min_distance:
                closest_words.append(dict_word)

        result_list.append((word, min_distance, closest_words))

    return result_list


sen1 = "The classic example provided in British publications."
sen2 = "Natural selection has gradually done away with them."


dictionary = word_list

closest_words1 = find_min_distance(sen1, dictionary)
closest_words2 = find_min_distance(sen2, dictionary)


print("\n\nFirst Sentence\n")
for item in closest_words1:
    print(item[0],"\t",item[1],"\t", item[2])

print("\n\nSecond Sentence\n")
for item in closest_words2:
    print(item[0],"\t",item[1],"\t", item[2])