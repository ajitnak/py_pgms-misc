def max_sub_array(arr):
	if len(arr) == 0:
		return None
	max_curr = max_glob = arr[0]
	for i in range(1, len(arr)):
		max_curr = max(arr[i], max_curr + arr[i])
		if max_curr > max_glob:
			max_glob = max_curr

	return max_glob

print max_sub_array([-2,3,2, 5, -10, 7,2])
	
