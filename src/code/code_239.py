class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 维护一个堆
        # 每次需要弹出一个元素，并插入一个元素，为了使得查找速度为O(1)
        # 增加一个list,用于记录元素在堆中的序号
        # 每次删除元素并添加元素后，重新堆化，时间为log(K)
        def heapify(heap, heap_idx, idx, heap_idx_map):
            fa_idx = idx // 2
            while heap[fa_idx] < heap[idx] and fa_idx > 0:
                # 向上堆化即可
                heap[fa_idx], heap[idx] = heap[idx], heap[fa_idx]
                heap_idx_map[heap_idx[idx]], heap_idx_map[heap_idx[fa_idx]] = heap_idx_map[heap_idx[fa_idx]], heap_idx_map[heap_idx[idx]]
                heap_idx[fa_idx], heap_idx[idx] = heap_idx[idx], heap_idx[fa_idx]
                idx = fa_idx
                fa_idx = idx // 2
            while idx * 2 <= k and idx > 0:
                max_idx = idx
                if heap[idx*2] > heap[max_idx]:
                    max_idx = idx * 2
                if idx * 2 + 1 <= k and heap[idx*2+1] > heap[max_idx]:
                    max_idx = idx * 2 + 1
                if max_idx != idx:
                    # 需要根据堆中的idx反查idx
                    heap_idx_map[heap_idx[idx]], heap_idx_map[heap_idx[max_idx]] = heap_idx_map[heap_idx[max_idx]], heap_idx_map[heap_idx[idx]]
                    heap_idx[idx], heap_idx[max_idx] = heap_idx[max_idx], heap_idx[idx]
                    heap[idx], heap[max_idx] = heap[max_idx], heap[idx]
                    idx = max_idx
                else:
                    break

        heap = [0]
        heap.extend(nums[:k])
        heap_idx = {}
        for i in xrange(1, k+1, 1):
            heap_idx[i] = i
        # 用新元素替换堆内元素，并执行堆化
        m = k // 2
        for i in xrange(m, 0, -1):
            max_idx = i
            if 2*i <= k and heap[2*i] > heap[max_idx]:
                max_idx = 2 * i
            if 2*i+1 <= k and heap[2*i+1] > heap[max_idx]:
                max_idx = 2 * i + 1
            if max_idx != i:
                heap[i], heap[max_idx] = heap[max_idx], heap[i]
                heap_idx[i], heap_idx[max_idx] = heap_idx[max_idx], heap_idx[i]

        heap_idx_map = {v: k for k, v in heap_idx.items()}
        # print heap, heap_idx, heap_idx_map
        rst = []
        for i in xrange(k, len(nums), 1):
            rst.append(heap[1])
            idx = heap_idx_map[i-k+1]
            heap[idx] = nums[i]
            # heap_idx[i+1] = idx
            # heap_idx_map[idx] = i + 1
            heap_idx_map[i+1] = idx
            heap_idx[idx] = i + 1
            del heap_idx_map[i-k+1]
            # print heap, heap_idx, idx, heap_idx_map
            heapify(heap, heap_idx, idx, heap_idx_map)
            # heap_idx = heap_idx[1:]
            # print 'aft', heap, heap_idx, heap_idx_map
        # print heap, heap_idx, rst
        rst.append(heap[1])
        return rst