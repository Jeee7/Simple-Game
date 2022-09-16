package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println("Guess The number?? ")

	rand.Seed(time.Now().UnixNano())
	min := 1
	max := 100
	var random = (rand.Intn(max-min+0) + min)
	var a int
	fmt.Scan(&a)
	var i = 0

	for i < 5 {
		if a == random {
			fmt.Println("Correct!! The number is : ", random)
			i = 5

		} else {
			fmt.Println("Wrong!!")
			fmt.Println("Try Again!")
			fmt.Scan(&a)
			i++

			if i == 5 {
				fmt.Println("Game Over!!, The number is : ", random)
			}

		}
	}
}
