import query_correction

if __name__ == "__main__":
    queryChecker = query_correction.QueryChecker('532b2cec37b643ce877268b4833da367')
    k = int(input('Enter K: '))

    while True:
        query = input('Enter query: ')
        results = queryChecker.correct(query, k)

        print ('Corrections: ')
        for i in range(len(results)):
            print(i+1, ':',results[i])


