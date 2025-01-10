def subset_2_word_with_any_order(words: str, sub: str) -> bool:
    w = [0] * 26
    s = [0] * 26

    for ch in words:
        w[ord(ch) - ord("a")] += 1
    for ch in sub:
        s[ord(ch) - ord("a")] += 1
    
    return all(ch_w >= ch_s for ch_w, ch_s in zip(w, s))
 
print(subset_2_word_with_any_order("leetcode", "eeo")) #True   
print(subset_2_word_with_any_order("leetcode", "eeeo")) #True      
print(subset_2_word_with_any_order("leetcode", "eeeeo")) #False      
print(subset_2_word_with_any_order("abcde", "acdbe")) #True      