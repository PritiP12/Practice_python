def minimum_removals(lst):

        total = sum(lst)
        count = 0
        if total % 2 == 0:
            print( 0)
        else:
            for i in lst:
                if (total - i) % 2 == 0:
                    count += 1
                    print( count)
                else:
                    count += 1
                    print(count )

minimum_removals([1,2,3,4,5])