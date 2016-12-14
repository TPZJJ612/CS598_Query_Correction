import query_correction
import re

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def load_dataset():
    queries = []
    corrections = []
    with open('combinedQueries.txt', 'r') as f:
        for line in f:
            row = line.rstrip().split('|||')
            if len(row) == 2:
                query, correction = row[0], row[1]
                if not hasNumbers(query):
                    queries.append(query)
                    corrections.append(correction)
    return queries, corrections


def precision_recall(queries, corrections, threshold):
    qc = query_correction.QueryChecker('532b2cec37b643ce877268b4833da367')
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    for i, query in enumerate(queries):
        if i >= threshold:
            break
        if i % 50 == 0:
            print ('Finished ', i)
            print (true_positive, true_negative, false_positive, false_negative)
        results = qc.correct(query, 7)
        if not results:
            continue

        corrected_query = results[0]
        ground_truth = corrections[i]

        if query == ground_truth:
            if corrected_query == query:
                true_positive += 1
            else:
                false_negative += 1
        else:
            if corrected_query != query:
                true_negative += 1
            else:
                false_positive += 1

    return true_positive, true_negative, false_positive, false_negative


def correction_test(queries, corrections, threshold):
    qc = query_correction.QueryChecker('532b2cec37b643ce877268b4833da367')
    top1 = 0
    top5 = 0
    top10 = 0
    count = 0

    for i, query in enumerate(queries):
        if i >= threshold:
            break
        if i % 50 == 0:
            print ('Finished ', i)
            print ('top1:', top1, 'top5:', top5, 'top10:', top10, 'valid words:', count)
        
        for k in [1, 5, 10]:
            corrected_queries = qc.correct(query, k)
            if not corrected_queries:
                continue

            if k == 1:
                count += 1

            if corrections[i] in corrected_queries:
                if k == 1:
                    top1 += 1
                elif k == 5:
                    top5 += 1
                else:
                    top10 += 1

    return top1, top5, top10, count

if __name__ == "__main__":
    queries, corrections = load_dataset()
#
#    true_positive, true_negative, false_positive, false_negative = precision_recall(queries, corrections, 10000)
#    print (true_positive, true_negative, false_positive, false_negative)
    #
    top1, top5, top10, count = correction_test(queries, corrections, 10000)
    print ('top1:', top1, 'top5:', top5, 'top10:', top10, 'valid words:', count)