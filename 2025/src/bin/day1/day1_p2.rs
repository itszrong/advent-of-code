// use std::env;
use std::fs;

fn main() {

    let contents = fs::read_to_string("src/bin/day1/data.txt")
        .expect("Should have been able to read the file");

    let lines = contents.lines();    
    let mut pos = 50;
    let mut counter = 0;

    for l in lines{
        let old_pos = pos;
        
        let value = l[1..].parse::<i32>().unwrap();
        let zero_count = if l.starts_with("L"){
            if old_pos > 0 && value >= old_pos {
                1 + (value - old_pos) / 100
            } else if old_pos == 0 {
                value / 100
            } else {
                0
            }
        } else {
            (old_pos + value) / 100
        };
    
        counter += zero_count;

        if l.starts_with("L") {
            pos = (old_pos - value) % 100;
            if pos < 0 {
                pos += 100;
            }
        } else {
            pos = (old_pos + value) % 100
        }



    }
    println!("{}", counter)
}

