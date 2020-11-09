import "container/heap"

type pair struct {
	dist  int
	point []int
}
type hp []pair

func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { return h[i].dist > h[j].dist }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(pair)) }
func (h *hp) Pop() interface{} {
	old := *h
	N := len(old)
	item := old[N-1]
	*h = old[0 : N-1]
	return item
}

func kClosest(points [][]int, k int) (ans [][]int) {
	h := make(hp, k)
	for i, p := range points[:k] {
		h[i] = pair{p[0]*p[0] + p[1]*p[1], p}
	}
	heap.Init(&h) // O(k) 初始化堆
	for _, p := range points[k:] {
		if dist := p[0]*p[0] + p[1]*p[1]; dist < h[0].dist {
			h[0] = pair{dist, p}
			heap.Fix(&h, 0) // 效率比 pop 后 push 要快
		}
	}
	for _, p := range h {
		ans = append(ans, p.point)
	}
	return
}
