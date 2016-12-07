import query_correction

if __name__ == "__main__":
    queryChecker = query_correction.QueryChecker()
    k = int(input('Enter K: '))

    while True:
        query = input('Enter query: ')
        results = queryChecker.correct(query.split(' '), k)

        corrected_queries = []
        for result in results:
            corrected_queries.append(' '.join(result[0]))

        print ('Corrections: ')
        for i, correction in enumerate(corrected_queries):
            print(i+1, ':',correction)


