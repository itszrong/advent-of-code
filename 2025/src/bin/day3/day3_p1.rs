use std::fs;
use std::collections::BinaryHeap;
use std::collections::BTreeMap;

fn main() {

    fn get_heap(line: &str, range: Vec<usize>) -> BinaryHeap<(u32, usize)> {
        let mut h = BinaryHeap::new();
        for (i, num) in line.chars().enumerate() {
            if range.contains(&i) {
                h.push((num.to_digit(10).unwrap(), line.len()-i));
           }
        }
        h
    }

    let contents = fs::read_to_string("src/bin/day3/data.txt")
        .expect("Should have been able to read the file");

    let mut sum = 0;
    let joltage_len = 2;
    for line in contents.lines() {
        let mut joltage_map = BTreeMap::new();
        let mut start = 0;
        let mut end = line.len();
        let mut range: Vec<usize> = (start..end).collect();
        for i in 0..joltage_len {
            let mut h = get_heap(line, range.clone());
            let c = h.pop();
            let k = line.len()-c.unwrap().1;
            let v = c.unwrap().0;
            joltage_map.insert(k ,v);
            if k < range.len()-(joltage_len-(i)) {
                start = k+1;
            } else {
                end = k;
            }
            range = (start..end).collect();
        }
        let joltage_str: String = joltage_map.values().map(|i| i.to_string()).collect::<String>();
        sum += joltage_str.parse::<i32>().unwrap();
        println!("{}, {}, {}", line, joltage_str, sum);
    }
}
