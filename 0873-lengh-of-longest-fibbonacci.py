class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Brute force version of the solution
        """
        sequences = []

        ##     Loop through all of the possible combinations of three integers and see if they
        ## add up together like we would expect a fibonacci sequence to be x(i) + x(i+1) = x(i+2)
        for a in range(len(arr) - 2):
            for b in range(a + 1, len(arr) - 1):
                for c in range(b + 1, len(arr)):
                    if arr[a] + arr[b] == arr[c]:
                        ## Append this item as a new sequence
                        sequences.append([a, b, c])

        for fib_idx in range(len(sequences)):
            nxt_id = sequences[fib_idx][-1] + 1
            while nxt_id < len(arr):
                a = sequences[fib_idx][-2]
                b = sequences[fib_idx][-1]
                c = nxt_id

                if arr[a] + arr[b] == arr[c]:
                    sequences[fib_idx].append(c)
                nxt_id += 1

        print(sequences)
        sequences = [len(s) for s in sequences]
        print(sequences)
        return max(sequences)
        
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_len = 0


        ##     Loop through all of the possible combinations of three integers and see if they
        ## add up together like we would expect a fibonacci sequence to be x(i) + x(i+1) = x(i+2)
        for a in range(len(arr) - 2):
            if len(arr) - a + 4 < max_len:
                break
            for b in range(a + 1, len(arr) - 1):
                if len(arr) - b + 3 < max_len:
                    break
                for c in range(b + 1, len(arr)):
                    if len(arr) - c + 2 < max_len:
                        break

                    if arr[a] + arr[b] == arr[c]:
                        seq_l = 3
                        x1 = arr[b]
                        x2 = arr[c]
                        nxt_id = c + 1
                        while nxt_id < len(arr):
                            if x1 + x2 == arr[nxt_id]:
                                seq_l += 1
                                x1 = x2
                                x2 = arr[nxt_id]
                            nxt_id += 1
                        if seq_l > max_len:
                            max_len = seq_l

        return max_len

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ## Build a hash map of the 
        arr_dict = {}
        idx = 0
        for a in arr:
            arr_dict[a] = idx
            idx += 1

        max_len = 0
        arr_len = len(arr)
        for x1 in range(arr_len):
            for x2 in range(x1+1, arr_len):
                cur_len = 2
                a = arr[x1]
                b = arr[x2]
                while (a + b) in arr_dict.keys():
                    cur_len += 1
                    c = a + b
                    a = b
                    b = c
                if cur_len != 2 and cur_len > max_len:
                    max_len = cur_len

        return max_len