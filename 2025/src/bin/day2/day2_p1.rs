// use std::env;
use std::fs;

fn main() {

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
            if n_str.len() % 2 == 0 {
                if n_str[..n_str.len()/2] == n_str[n_str.len()/2..] {
                    invalid.push(n);
                }
            } 
        }
    }
    let mut sum: i64 = 0;
    for num in invalid.iter() {
        sum += num
    }
    println!("{}", sum)
}

