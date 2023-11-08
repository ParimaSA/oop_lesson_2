def gen_comb_list(list_set):
    """
        Parameters:
            list_set: a list of lists where each contains at least one element

        Returns:
            a list of lists, each of which is made from a combination of elements in each list in list_set

        Examples:
            gen_comb_list([[1, 2, 3]]) returns [[1], [2], [3]]
            gen_comb_list([[1, 2, 3], [4, 5]]) returns [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]]
            gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]) returns [[1, 4, 6], [2, 4, 6], [3, 4, 6], [1, 5, 6], [2, 5, 6], [3, 5, 6], [1, 4, 7], [2, 4, 7], [3, 4, 7], [1, 5, 7], [2, 5, 7], [3, 5, 7], [1, 4, 8], [2, 4, 8], [3, 4, 8], [1, 5, 8], [2, 5, 8], [3, 5, 8]]
    """

    num_list = [len(x) for x in list_set]
    num_now = [0 for x in num_list]
    answer = []
    while num_now[-1] < num_list[-1]:
        add = []
        for i in range(len(list_set)):
            add.append(list_set[i][num_now[i]])
        answer.append(add)
        num_now[0] += 1
        for i in range(len(list_set) - 1):
            if num_now[i] == num_list[i]:
                num_now[i] = 0
                num_now[i + 1] += 1

    return answer
