use std::fs;

fn main() {
    let contents = fs::read_to_string("src/bin/day5/data.txt")
        .expect("Should have been able to read the file");

    let mut fresh = 0;
    let mut ranges_vec: Vec<(i64, i64)> = Vec::new();
    let components = contents.split("\n\n").collect::<Vec<&str>>();
    let ranges = components[0];
    for range in ranges.lines() {
        let start_end = range.split('-').collect::<Vec<&str>>();
        ranges_vec.push((start_end[0].parse::<i64>().unwrap(),start_end[1].parse::<i64>().unwrap()));
    }
    let nums = components[1].split('\n').collect::<Vec<&str>>();
    for num in nums.iter() {
        for (i, j) in ranges_vec.iter() {
            if i <= &num.parse::<i64>().unwrap() && &num.parse::<i64>().unwrap() <= j {
                fresh += 1;
                break
            }
        }
    }
    
    println!("{:?}", fresh);
}
