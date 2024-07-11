import re
import webbrowser
import numpy as np


class Article:
    def __init__(self, number, name, translated=False, references=None):
        self.number = number
        self.name = name
        self.translated = translated
        if references is None:
            references = []
        self.references = references

    def print_article(self):
        if self.references:
            print(f"Article {self.number}: {self.name}. References to: {', '.join(self.references)}.")
        else:
            print(f"Article {self.number}: {self.name}.")


"""
class Reference:
    def __init__(self, source, destination, kind):
        self.source = source
        self.destination = destination
        self.kind = kind

    def print_reference(self):
        print(f"Reference from {self.source} to {self.destination} of kind {self.kind}")
"""

articles_list = {
    1: Article(1, "Subject-matter and objectives"),
    2: Article(2, "Material scope"),
    3: Article(3, "Territorial scope"),
    4: Article(4, "Definitions"),
    5: Article(5, "Principles relating to processing of personal data", translated=True),
    6: Article(6, "Lawfulness of processing", translated=True),
    7: Article(7, "Conditions for consent", translated=True),
    8: Article(8, "Conditions applicable to child's consent in relation to information society services",
               translated=True),
    9: Article(9, "Processing of special categories of personal data", translated=True),
    10: Article(10, "Processing of personal data relating to criminal convictions and offences", translated=True),
    11: Article(11, "Processing which does not require identification"),
    12: Article(12,
                "Transparent information, communication and modalities for the exercise of the rights of the data subject"),
    13: Article(13, "Information to be provided where personal data are collected from the data subject",
                translated=True),
    14: Article(14, "Information to be provided where personal data have not been obtained from the data subject",
                translated=True),
    15: Article(15, "Right of access by the data subject", translated=True),
    16: Article(16, "Right to rectification", translated=True),
    17: Article(17, "Right to erasure ('right to be forgotten')", translated=True),
    18: Article(18, "Right to restriction of processing"),
    19: Article(19,
                "Notification obligation regarding rectification or erasure of personal data or restriction of processing"),
    20: Article(20, "Right to data portability", translated=True),
    21: Article(21, "Right to object", translated=True),
    22: Article(22, "Automated individual decision-making, including profiling"),
    23: Article(23, "Restrictions"),
    24: Article(24, "Responsibility of the controller"),
    25: Article(25, "Data protection by design and by default", translated=True),
    26: Article(26, "Joint controllers"),
    27: Article(27, "Representatives of controllers or processors not established in the Union"),
    28: Article(28, "Processor"),
    29: Article(29, "Processing under the authority of the controller or processor"),
    30: Article(30, "Records of processing activities"),
    31: Article(31, "Cooperation with the supervisory authority"),
    32: Article(32, "Security of processing", translated=True),
    33: Article(33, "Notification of a personal data breach to the supervisory authority"),
    34: Article(34, "Communication of a personal data breach to the data subject"),
    35: Article(35, "Data protection impact assessment"),
    36: Article(36, "Prior consultation"),
    37: Article(37, "Designation of the data protection officer"),
    38: Article(38, "Position of the data protection officer"),
    39: Article(39, "Tasks of the data protection officer", translated=True),
    40: Article(40, "Codes of conduct"),
    41: Article(41, "Monitoring of approved codes of conduct"),
    42: Article(42, "Certification"),
    43: Article(43, "Certification bodies"),
    44: Article(44, "General principle for transfers", translated=True),
    45: Article(45, "Transfers on the basis of an adequacy decision"),
    46: Article(46, "Transfers subject to appropriate safeguards", translated=True),
    47: Article(47, "Binding corporate rules"),
    48: Article(48, "Transfers or disclosures not authorised by Union law"),
    49: Article(49, "Derogations for specific situations", translated=True),
    50: Article(50, "International cooperation for the protection of personal data"),
    51: Article(51, "Supervisory authority"),
    52: Article(52, "Independence"),
    53: Article(53, "General conditions for the members of the supervisory authority"),
    54: Article(54, "Rules on the establishment of the supervisory authority"),
    55: Article(55, "Competence"),
    56: Article(56, "Competence of the lead supervisory authority"),
    57: Article(57, "Tasks"),
    58: Article(58, "Powers", translated=True),
    59: Article(59, "Activity reports"),
    60: Article(60,
                "Cooperation between the lead supervisory authority and the other supervisory authorities concerned"),
    61: Article(61, "Mutual assistance"),
    62: Article(62, "Joint operations of supervisory authorities"),
    63: Article(63, "Consistency mechanism"),
    64: Article(64, "Opinion of the Board"),
    65: Article(65, "Dispute resolution by the Board"),
    66: Article(66, "Urgency procedure"),
    67: Article(67, "Exchange of information"),
    68: Article(68, "European Data Protection Board"),
    69: Article(69, "Independence"),
    70: Article(70, "Tasks of the Board"),
    71: Article(71, "Reports"),
    72: Article(72, "Procedure"),
    73: Article(73, "Chair"),
    74: Article(74, "Tasks of the Chair"),
    75: Article(75, "Secretariat"),
    76: Article(76, "Confidentiality"),
    77: Article(77, "Right to lodge a complaint with a supervisory authority"),
    78: Article(78, "Right to an effective judicial remedy against a supervisory authority"),
    79: Article(79, "Right to an effective judicial remedy against a controller or processor"),
    80: Article(80, "Representation of data subjects"),
    81: Article(81, "Suspension of proceedings"),
    82: Article(82, "Right to compensation and liability"),
    83: Article(83, "General conditions for imposing administrative fines"),
    84: Article(84, "Penalties"),
    85: Article(85, "Processing and freedom of expression and information"),
    86: Article(86, "Processing and public access to official documents"),
    87: Article(87, "Processing of the national identification number"),
    88: Article(88, "Processing in the context of employment"),
    89: Article(89,
                "Safeguards and derogations relating to processing for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes"),
    90: Article(90, "Obligations of secrecy"),
    91: Article(91, "Existing data protection rules of churches and religious associations"),
    92: Article(92, "Exercise of the delegation"),
    93: Article(93, "Committee procedure"),
    94: Article(94, "Repeal of Directive 95/46/EC"),
    95: Article(95, "Relationship with Directive 2002/58/EC"),
    96: Article(96, "Relationship with previously concluded Agreements"),
    97: Article(97, "Commission reports"),
    98: Article(98, "Review of other Union legal acts on data protection"),
    99: Article(99, "Entry into force and application"),
}

references_list = {
    1: [],
    2: ["Art. 98", "Articles 12-15"],
    3: [],
    4: [],
    5: ["Art. 89(1)"],
    6: ["Art. 9", "Art. 10", "Art. 23(1)", "Chapter IX (Articles 85-91)"],
    7: [],
    8: ["Art. 6(1)(a)"],
    9: ["Art. 89(1)"],
    10: ["Art. 6(1)"],
    11: ["Articles 15-20"],
    12: ["Art. 11", "Art. 13", "Art. 14", "Art. 15", "Art. 16", "Art. 17", "Art. 18", "Art. 19", "Art. 20", "Art. 21",
         "Art. 22", "Art. 34", "Art. 92"],
    13: ["Art. 6(1)(f)", "Art. 46", "Art. 47", "Art. 49(1)", "Art. 6(1)(a)", "Art. 9(2)(a)", "Art. 22(1) and 22(4)"],
    14: ["Art. 6(1)(f)", "Art. 46", "Art. 47", "Art. 49(1)", "Art. 6(1)(a)", "Art. 9(2)(a)", "Art. 22(1) and 22(4)",
         "Art. 89(1)"],
    15: ["Art. 22(1) and 22(4)", "Art. 46"],
    16: [],
    17: ["Art. 6(1)(a)", "Art. 8(1)", "Art. 9(2)(a) and Art. 9(2)(h) and Art. 9(2)(i) and Art. 9(3)",
         "Art. 21(1) and 21(2)", "Art. 89(1)"],
    18: ["Art. 21(1)"],
    19: ["Art. 16", "Art. 17(1)", "Art. 18"],
    20: ["Art. 6(1)(a)", "Art. 9(2)(a)", "Art. 6(1)(b)", "Art. 17"],
    21: ["Art. 6(1)(e) and Art. 6(1)(f)", "Art. 89(1)"],
    22: ["Art. 9(1) and Art. 9(2)(a) and Art. 9(2)(g)"],
    23: ["Art. 5", "Articles 12-22", "Art. 34"],
    24: ["Art. 40", "Art. 42"],
    25: ["Art. 42"],
    26: ["Art. 13", "Art. 14"],
    27: ["Art. 3(2)", "Art. 9(1)", "Art. 10"],
    28: ["Art. 32", "Chapter III (Articles 12-23)", "Articles 32-36", "Art. 40", "Art. 42", "Art. 43", "Art. 63",
         "Art. 82", "Art. 83", "Art. 84", "Art. 93(2)"],
    29: [],
    30: ["Art. 9(1)", "Art. 10", "Art. 32(1)", "Art. 49(1)"],
    31: [],
    32: ["Art. 40", "Art. 42"],
    33: ["Art. 55"],
    34: ["Art. 33(3)(b) and Art. 33(3)(c) and Art. 33(3)(d)"],
    35: ["Art. 6(1)(c) and Art. 6(1)(e)", "Art. 9(1)", "Art. 10", "Art. 40", "Art. 63", "Art. 68"],
    36: ["Art. 35", "Art. 58"],
    37: ["Art. 9", "Art. 10", "Art. 39"],
    38: ["Art. 39"],
    39: ["Art. 35", "Art. 36"],
    40: ["Art. 3", "Art. 24", "Art. 25", "Art. 32", "Art. 41(1)", "Art. 46(2)(e)", "Art. 55", "Art. 56", "Art. 63",
         "Art. 77", "Art. 79", "Art. 93(2)"],
    41: ["Art. 40", "Art. 57", "Art. 58", "Art. 63", "Chapter VIII (Articles 77-84)"],
    42: ["Art. 3", "Art. 43", "Art. 46(2)(f)", "Art. 55", "Art. 56", "Art. 58(3)", "Art. 63"],
    43: ["Art. 42(1) and Art. 42(5)", "Art. 55", "Art. 56", "Art. 57", "Art. 58", "Art. 63",
         "Chapter VIII (Articles 77-84)", "Art. 92", "Art. 93(2)"],
    44: [],
    45: ["Art. 93(2) and 93(3)", "Articles 46-49"],
    46: ["Art. 40", "Art. 42", "Art. 45(3)", "Art. 47", "Art. 63", "Art. 93(2)"],
    47: ["Art. 13", "Art. 14", "Art. 22", "Art. 37", "Art. 63", "Art. 79", "Art. 93(2)"],
    48: [],
    49: ["Art. 13", "Art. 14", "Art. 30", "Art. 45", "Art. 46"],
    50: [],
    51: ["Chapter VII (Articles 60-76)", "Art. 63"],
    52: [],
    53: [],
    54: [],
    55: ["Art. 6(1)(c) and Art. 6(1)(e)", "Art. 56"],
    56: ["Art. 55", "Art. 60", "Art. 61", "Art. 62"],
    57: ["Art. 28(8)", "Art. 35(4)", "Art. 36(2)", "Art. 40(1) and Art. 40(5)", "Art. 41",
         "Art. 42(1) and Art. 42(5) and Art. 42(7)", "Art. 43", "Art. 46(2)(d) and Art. 46(3)", "Art. 47", "Art. 58(2)",
         "Art. 80"],
    58: ["Art. 16", "Art. 17", "Art. 18", "Art. 19", "Art. 28(8)", "Art. 36", "Art. 40(5)", "Art. 42", "Art. 43",
         "Art. 46(2)(d) and Art. 46(3)(a) and Art. 46(3)(b)", "Art. 47", "Chapter VII (Articles 60-76)", "Art. 83"],
    59: ["Art. 58(2)"],
    60: ["Art. 61", "Art. 62", "Art. 63", "Art. 66"],
    61: ["Art. 55(1)", "Art. 66(1) and Art. 66(2)", "Art. 93(2)"],
    62: ["Art. 55", "Art. 56(1) and Art. 56(4)", "Art. 66(1) and Art. 66(2)"],
    63: [],
    64: ["Art. 28(8)", "Art. 35(4)", "Art. 40(7)", "Art. 41(3)", "Art. 42(5)", "Art. 43(3)",
         "Art. 46(2)(d) and Art. 46(3)(a)", "Art. 47", "Art. 61", "Art. 62", "Art. 65(1)"],
    65: ["Art. 60(4) and Art. 60(7) and Art. 60(8) and Art. 60(9)", "Art. 64"],
    66: ["Art. 60", "Art. 63", "Art. 64", "Art. 65"],
    67: ["Art. 64", "Art. 93(2)"],
    68: ["Art. 65"],
    69: ["Art. 70", "Art. 71"],
    70: ["Art. 12(7)", "Art. 17(2)", "Art. 22(2)(e)", "Art. 33(1) and Art. 33(2)", "Art. 34(1)", "Art. 40", "Art. 42",
         "Art. 43", "Art. 47", "Art. 49(1)", "Art. 54(2)", "Art. 58(1) and Art. 58(2) and Art. 58(3)", "Art. 64",
         "Art. 65", "Art. 66", "Art. 76", "Art. 83", "Art. 93"],
    71: ["Art. 65", "Art. 70(1)(l)"],
    72: [],
    73: [],
    74: ["Art. 63", "Art. 65"],
    75: [],
    76: [],
    77: ["Art. 78"],
    78: ["Art. 55", "Art. 56", "Art. 77"],
    79: ["Art. 77"],
    80: ["Art. 77", "Art. 78", "Art. 79", "Art. 82"],
    81: [],
    82: ["Art. 79(2)"],
    83: ["Art. 5", "Art. 6", "Art. 7", "Art. 8", "Art. 9", "Art. 11", "Articles 12-22", "Art. 25", "Art. 32", "Art. 39",
         "Art. 40", "Art. 41(4)", "Art. 42", "Art. 43", "Articles 44-49", "Art. 58(1) and Art. 58(2)",
         "Chapter IX (Articles 85-91)"],
    84: ["Art. 83"],
    85: ["Chapter II (Articles 5-11)", "Chapter III (Articles 12-23)", "Chapter IV (Articles 24-43)",
         "Chapter V (Articles 44-50)", "Chapter VI (Articles 51-59)", "Chapter VII (Articles 60-76)",
         "Chapter IX (Articles 85-91)"],
    86: [],
    87: [],
    88: [],
    89: ["Art. 15", "Art. 16", "Art. 18", "Art. 19", "Art. 20", "Art. 21"],
    90: ["Art. 58(1)(e) and Art. 58(1)(f)"],
    91: ["Chapter VI (Articles 51-59)"],
    92: ["Art. 12(8)", "Art. 43(8)"],
    93: [],
    94: [],
    95: [],
    96: [],
    97: ["Art. 45(3)", "Chapter V (Articles 44-50)", "Chapter VII (Articles 60-76)"],
    98: [],
    99: []
}

graph_matrix = np.zeros((100, 100), dtype=int)


def setup_graph_matrix(article_with_references: dict[int, Article]):
    for article_number, article in article_with_references.items():
        graph_matrix[0][article_number] = int(article_number)
        graph_matrix[article_number][0] = int(article_number)
        if article.references:
            for reference in article.references:
                regex1 = r"^Art.\ \d+"
                regex2 = r"Articles \d+-\d+"
                match1 = re.search(pattern=regex1, string=reference)
                if match1:
                    match1 = match1.string
                    match1 = re.sub(r"\(.+\)", "", match1)
                    match1 = re.sub(r"\D", "", match1)
                    reference_number = int(match1)
                    graph_matrix[article_number][reference_number] = 1
                else:
                    match2 = re.search(pattern=regex2, string=reference)
                    if match2:
                        match2 = match2.string
                        match2 = re.sub(r"[^\d+\-\d+]", "", match2)
                        match2 = match2.split("-")
                        candidate_number1 = int(match2[0])
                        candidate_number2 = int(match2[1])
                        for i in range(candidate_number1, candidate_number2 + 1):
                            graph_matrix[article_number][i] = 1
    print("Graph matrix has been set up.\n")
    with np.printoptions(threshold=np.inf):
        print(graph_matrix)


def setup_articles_with_references() -> dict[int, Article]:
    articles_with_references = {}
    for value in articles_list.values():
        if value.number in references_list:
            value.references = references_list[value.number]
        articles_with_references[value.number] = value
    setup_graph_matrix(articles_with_references)
    return articles_with_references


def article_options(article_with_references: dict[int, Article], article_number: int):
    choice = ""
    while choice != "b":
        print(f"Article {article_number}")
        print(f"{article_with_references[article_number].name}\n")
        print('What would you like to do?')
        print('t) Read the full text of this article')
        print('r) Jump to one of the articles mentioned by this article')
        print('b) Return to the last "visited" article (if any)')
        choice = input('')
        if choice == 't':
            print("Opening the full text of the article in a new tab of your default browser...")
            webbrowser.open(f"https://gdpr-info.eu/art-{article_number}/", new=2)
        elif choice == 'r':
            if article_with_references[article_number].references:
                print(f"This article mentions: {', '.join(article_with_references[article_number].references)}.")
                candidates_list = article_with_references[article_number].references
                choosable_article_numbers = []
                for candidate in candidates_list:
                    regex1 = r"^Art.\ \d+"
                    regex2 = r"Articles \d+-\d+"
                    match1 = re.search(pattern=regex1, string=candidate)
                    if match1:
                        match1 = match1.string
                        match1 = re.sub(r"\(.+\)", "", match1)
                        match1 = re.sub(r"\D", "", match1)
                        candidate_number = int(match1)
                        choosable_article_numbers.append(candidate_number)
                    else:
                        match2 = re.search(pattern=regex2, string=candidate)
                        if match2:
                            match2 = match2.string
                            match2 = re.sub(r"[^\d+\-\d+]", "", match2)
                            match2 = match2.split("-")
                            candidate_number1 = int(match2[0])
                            candidate_number2 = int(match2[1])
                            for i in range(candidate_number1, candidate_number2 + 1):
                                choosable_article_numbers.append(i)
                callee_article_number = int(input('Please enter the number of the article you want to jump to: '))
                if callee_article_number in choosable_article_numbers:
                    article_options(article_with_references, callee_article_number)
                else:
                    print("Invalid article number. Please try again.\n")
            else:
                print("This article doesn't mention other articles.\n")
        elif choice == 'b':
            return 0
        else:
            print("Invalid option. Please try again.\n")


def GDPR_navigator(article_with_references: dict[int, Article]):
    print('Welcome to the GDPR Navigator!')
    article_number = -1
    while article_number != 0:
        print(
            'There are 99 articles in the GDPR. Please enter the number of the article you are interested in, or 0 to return to the main menu.')
        article_number = int(input(''))
        if article_number in article_with_references:
            article_options(article_with_references, article_number)
        elif article_number == 0:
            print("Returning to the main menu...\n")
            return 0
        else:
            print("Invalid article number. Please try again.\n")


def print_articles_list(articles_with_references: dict[int, Article]):
    count = 0
    for number, article in articles_with_references.items():
        if article.translated:
            count += 1
            article.print_article()
    print(f"\n{count} articles have been translated into Legalease, so far.\n")


def main():
    articles_with_references = setup_articles_with_references()
    choice = -1
    while choice != 0:
        print('Hello, how can I help you?')
        print('1) Navigate between GDPR articles')
        print('2) Print the list of articles that have been translated into Legalease, so far')
        print('0) Terminate the program')
        choice = int(input(''))
        if choice == 1:
            GDPR_navigator(articles_with_references)
        elif choice == 2:
            print_articles_list(articles_with_references)
        elif choice == 0:
            print("Goodbye!")
            return 0
        else:
            print('Invalid choice\n')


if __name__ == '__main__':
    main()
