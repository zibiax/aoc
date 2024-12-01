package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
    "strconv"
    "strings"
    "time"
)

func readInput(filename string) []string {
    file, err := os.Open(filename)
    if err != nil {
        panic(err)
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines
}

func first(input []string) int {
    total := 0
    var left, right []int

    for _, line := range input {
        parts := strings.Fields(line)
        if len(parts) == 2 {
            l1, _ := strconv.Atoi(parts[0])
            r1, _ := strconv.Atoi(parts[1])
            left = append(left, l1)
            right = append(right, r1)
        }
    }

    sort.Ints(left)
    sort.Ints(right)

    for len(left) > 0 && len(right) > 0 {
        l1 := left[0]
        r1 := right[0]
        diff := l1 - r1
        if diff < 0 {
            diff = -diff
        }
        total += diff
        left = left[1:]
        right = right[1:]
    }

    return total
}

func second(input []string) int {
    total := 0
    var left, right []int

    for _, line := range input {
        parts := strings.Fields(line)
        if len(parts) == 2 {
            l1, _ := strconv.Atoi(parts[0])
            r1, _ := strconv.Atoi(parts[1])
            left = append(left, l1)
            right = append(right, r1)
        }
    }

    sort.Ints(left)
    sort.Ints(right)

    for _, i := range left {
        times := 0
        for _, x := range right {
            if i == x {
                times++
            }
        }
        score := i * times
        total += score
    }

    return total
}

func main() {
    data := readInput("input.txt")
    
    start := time.Now()
    result1 := first(data)
    duration1 := time.Since(start)
    fmt.Println(result1)
    fmt.Printf("%v\n", duration1)

    start = time.Now()
    result2 := second(data)
    duration2 := time.Since(start)
    fmt.Println(result2)
    fmt.Printf("%v\n", duration2)
}
