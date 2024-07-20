package sort

func QuickSort(arr []int) []int {
	return quickSort(arr, 0, len(arr)-1)
}

func quickSort(arr []int, low int, high int) []int {
	if low < high {
		arr, p := partition(arr, low, high)
		arr = quickSort(arr, low, p-1)
		arr = quickSort(arr, p+1, high)
	}
	return arr
}

func QuickSortWithMerge(arr []int) []int {
	return quickSortWithMerge(arr, 0, len(arr)-1)
}

func quickSortWithMerge(arr []int, low int, high int) []int {
	if low < high {
		if len(arr) < 10 {
			arr = MergeSort(arr)
		} else {
			arr, p := partition(arr, low, high)
			arr = quickSort(arr, low, p-1)
			arr = quickSort(arr, p+1, high)
		}
	}
	return arr
}

func partition(arr []int, left int, right int) ([]int, int) {
	pivot := arr[right]
	// Position of the smaller element
	i := left
	for j := left; j < right; j++ {
		if arr[j] <= pivot {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}

	arr[i], arr[right] = arr[right], arr[i]
	return arr, i
}
