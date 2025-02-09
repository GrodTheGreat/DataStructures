package main

import "fmt"

type StaticArray struct {
	arr []int
	capacity int
	size int
}

func newStaticArray(capacity int) *StaticArray {
	return &StaticArray {
		arr: make([]int, capacity),
		capacity: capacity,
		size: 0,
	}
}

func (a *StaticArray) get(index int) (int, error) {
	if index < 0 {
		return 0, fmt.Errorf("index out of bounds")
	}
	if index > a.capacity {
		return 0, fmt.Errorf("index out of bounds")
	}
	return a.arr[index], nil
}

func (a *StaticArray) set(index int, value int) error {
	if index < 0 {
		return fmt.Errorf("index out of bounds")
	}
	if index > a.capacity {
		return fmt.Errorf("index out of bounds")
	}
	a.arr[index] = value
	a.size++
	return nil
}

func (a *StaticArray) length() int {
	return a.size
}

func (a *StaticArray) remove(index int) error {
	if index < 0 {
		return fmt.Errorf("index out of bounds")
	}
	if index > a.capacity {
		return fmt.Errorf("index out of bounds")
	}
	a.arr[index] = 0
	a.size--
	return nil
} 

func main() {

}