import query_correction

if __name__ == "__main__":
    queryChecker = query_correction.QueryChecker()
    k = int(input('Enter K: '))

    while True:
        query = input('Enter query: ')
        results = queryChecker.correct(query.split(' '), k)

        print ('Corrections: ')
        for i in range(len(results)):
            print(i+1, ':',results[i]['res'])


