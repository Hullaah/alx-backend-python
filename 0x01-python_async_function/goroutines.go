package main

import (
	"fmt"
	"math/rand"
	// "sync"
	"time"
)

func wait_random(maxDelay int) float64 {
	delay := rand.Float64() * float64(maxDelay)
	time.Sleep(time.Second * time.Duration(delay))
	return delay
}

func wait_n(n int, maxDelay int) []float64 {
	delays := make([]float64, n)
	ch := make(chan float64)
	for i := 0; i < n; i++ {
		go func(ch chan<- float64) {
			ch <- wait_random(maxDelay)
		}(ch)
	}
	for i := 0; i < n; i++ {
		delays[i] = <-ch
	}
	return delays
}

func main() {
	// var wg sync.WaitGroup
	// duration := map[int]int{
	// 	5: 5,
	// 	7: 10,
	// 	0: 10,
	// }

	// for k, v := range duration {
	// 	wg.Add(1)
	// 	go func() {
	// 		defer wg.Done()
	// 		fmt.Println(wait_n(v, k))
	// 	}()
	// }

	// wg.Wait()

	fmt.Println(wait_n(5, 5))
	fmt.Println(wait_n(10, 7))
	fmt.Println(wait_n(10, 0))
}
