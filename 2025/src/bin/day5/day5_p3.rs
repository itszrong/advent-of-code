use std::fs;

fn main() {
    let contents = fs::read_to_string("src/bin/day5/data.txt")
        .expect("Should have been able to read the file");

    let mut fresh = 0;
    let (ranges_block, _) = contents.split_once("\n\n").unwrap();
    let mut ranges: Vec<(i64, i64)> = ranges_block
        .lines()
        .filter(|line| !line.trim().is_empty())
        .map(|line| {
            let (s, e) = line.split_once('-').unwrap();
            (s.parse::<i64>().unwrap(), e.parse::<i64>().unwrap())
        })
        .collect();

    let mut prev: i64 = -1;
    ranges.sort_unstable_by_key(|&(s, e)| (s, e));
    for &(mut s, e) in ranges.iter() {
        if s <= prev {
            s = prev + 1;
        }
        if s <= e {
            fresh += e-s+1;
            prev = e;
        }
    }
    
    println!("{:?}", fresh);
}