// use std::env;
use std::fs;
use counter::Counter;

fn main() {

    fn check(smallest_window: usize, max_window: usize, n_str: String) -> bool {
        let mut invalid_str: bool  = false;
        for i in smallest_window..(max_window+1) {
            let str_match: &str = &n_str[..i];
            let mut count = 0;
            for j in 0..(n_str.len()/i) {
                if n_str.len() % i != 0 {
                    continue
                }
                if str_match == &n_str[j*(i)..(j+1)*(i)] {
                    count += 1;
                }
            }
            if count == n_str.len()/i {
                invalid_str = true;
                break
            } else {

            }
        }
        invalid_str
    }

    let contents = fs::read_to_string("src/bin/day2/data.txt")
        .expect("Should have been able to read the file");

    let ranges: Vec<&str> = contents.split(',').collect();
    let mut invalid: Vec<i64> = vec![];

    for range in ranges.iter() {
        let start_end: Vec<&str> = range.split('-').collect();
        let start: i64 = start_end[0].parse::<i64>().unwrap();
        let end: i64 = start_end[1].parse::<i64>().unwrap();
        for n in start..=end {
            let n_str = n.to_string();
            
            let counts = n_str.chars().collect::<Counter<_>>();
            let min_count = counts.values().min().unwrap();
            let max_count = counts.values().max().unwrap();
            
            if n_str.len() == 1 {
                continue
            }

            if *min_count == n_str.len() {
                if counts.keys().len() == 1 {
                    invalid.push(n);
                    continue
                }
            }
            
            if *min_count > 1 {
                let smallest_window = n_str.len() / max_count;
                let max_window = n_str.len() / 2;
                let invalid_str_return = check(smallest_window, max_window, n_str);
                if invalid_str_return {
                    invalid.push(n);
                }
                continue
            }

        }
    }
    let mut sum: i64 = 0;
    for num in invalid.iter() {
        sum += num
    }
    println!("{:?}", invalid);
    println!("{}", sum)
}

