## CS598 Final Project -- Python Module for Query Correction

Since Microsoft Project Oxford Web Language Model API is used in this project, 
You will need a subscription key to use this services. There are limits to 
the number of calls one can make to this service, and rate limits. This module 
does not concern itself with these limits.

You only need query_correcton.py and words.txt to run this module. 

Python 3.3 should be used to run the module

Parameters you need:

key: the subscription key

query: the query you want to correct

k: how many corrections you want 

Example uses:

    > key = 'ABCVJFIJDFOAJDF'
    > query = 'goverment home page of illinoisstate'
    > k = 7
    > import query_correction
    > qc = query_correction.QueryChecker(key)
    > print(qc.correct(query, k))
    
Demo uses:

    python userdemo.py

