use std::fs;
use std::collections::BinaryHeap;

fn main() {
    let contents = fs::read_to_string("src/bin/day5/data.txt")
        .expect("Should have been able to read the file");

    let mut fresh = 0;
    let mut ranges_heap: BinaryHeap<(i64, i64)> = BinaryHeap::new();
    let components = contents.split("\n\n").collect::<Vec<&str>>();
    let ranges = components[0];
    for range in ranges.lines() {
        let start_end = range.split('-').collect::<Vec<&str>>();
        let start = start_end[0].parse::<i64>().unwrap().clone();
        let end = start_end[1].parse::<i64>().unwrap().clone();
        ranges_heap.push((-start, -end));
    };

    let mut prev = (-1, -1);
    while !ranges_heap.is_empty() {
        let mut curr = ranges_heap.pop().unwrap();
        curr.0 = -curr.0;
        curr.1 = -curr.1;
        if curr.0 <= prev.1 {
            curr.0 = prev.1 + 1;
        }
        if curr.0 <= curr.1 {
            fresh += curr.1-curr.0+1;
            prev = curr.clone();
        }
    }
    
    println!("{:?}", fresh);
}