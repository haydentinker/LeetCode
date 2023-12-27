func firstUniqChar(s string) int {
    charCount := make(map[byte]int)
     for _, ch := range s {
        charCount[byte(ch)]++
    }
    for index,element:=range s{
        if charCount[byte(element)]==1{
            return index
        }
    }
    return -1
}