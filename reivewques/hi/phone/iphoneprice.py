
a = [[1,2,3],[[[]]],[4],5,[[[6,7]]]]
def concatList(data):
    results = []
    for rec in data:

        if type(rec) == list:
            results += rec

            results = concatList(results)
        else:

            results.append(rec)
    return results

final_list=concatList(a)
print(final_list)