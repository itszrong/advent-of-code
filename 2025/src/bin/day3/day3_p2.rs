use std::fs;
use min_max_heap::MinMaxHeap;
use std::collections::BTreeMap;

fn main() {

    fn get_heap(line: &str, range: Vec<usize>) -> MinMaxHeap<(u32, usize)> {
        let mut h = MinMaxHeap::new();
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
    let joltage_len = 12;
    for line in contents.lines() {
        let mut joltage_map = BTreeMap::new();
        let start = 0;
        let end = line.len();
        let mut range: Vec<usize> = (start..end).collect();
        while joltage_map.len() < joltage_len && !range.is_empty() {
            let mut h = get_heap(line, range.clone());
            if h.is_empty() {
                break;
            }
            let c: Option<(u32, usize)>;

            let all_same_x = {
                if let Some(&(first_x, _)) = h.peek_min() {
                    h.iter().all(|(x, _)| *x == first_x)
                } else {
                    true
                }
            };

            if all_same_x {
                c = h.pop_min();
            } else {
                c = h.pop_max();
            }
            let k = line.len()-c.unwrap().1;
            let v = c.unwrap().0;
            joltage_map.insert(k ,v);
            let after = range.iter().map(|&x| x > k).collect::<Vec<_>>().into_iter().filter(|x| *x).count();
            let index = range.iter().position(|x| *x == k).expect("not found");
            let remaining_needed = joltage_len - joltage_map.len();

            if after >= remaining_needed {
                range = range[index+1..].to_vec();
            } else {
                let add_range = range[index + 1..].to_vec();
            
                for &idx in add_range.iter().take(remaining_needed) {
                    let digit = (line.as_bytes()[idx] - b'0') as u32;
                    joltage_map.insert(idx, digit);
                }
            
                range = range[..index].to_vec();
            }
        }
        let joltage_str: String = joltage_map.values().map(|i| i.to_string()).collect::<String>();
        sum += joltage_str.parse::<i64>().unwrap();
        println!("{}, {}, {}", line, joltage_str, sum);
    }
}
