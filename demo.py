import query_correction

if __name__ == "__main__":
    query = 'home page of illinoisstate'
    queryChecker = query_correction.QueryChecker()
    print (queryChecker.correct(query.split(" "), 2))


