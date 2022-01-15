class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

	    fresh = set()
	    unvisited_rotten = set()
	    for i, row in enumerate(grid):
		    for j, cell in enumerate(row):
			    if cell==2:
				    unvisited_rotten.add((i, j))
			    elif cell: # not 0 or 2
				    fresh.add((i, j))
				
	    minutes = 0

	    while fresh and unvisited_rotten:

		    unvisited_rotten = set().union(*[fresh & {(i, j+1), (i+1, j), (i-1, j), (i, j-1)} for i, j in unvisited_rotten])
		    fresh -= unvisited_rotten

		    minutes += 1

	    return -1 if fresh else minutes
        