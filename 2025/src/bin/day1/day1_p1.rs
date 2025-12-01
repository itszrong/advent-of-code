// use std::env;
use std::fs;

fn main() {

    let contents = fs::read_to_string("src/bin/day1/data.txt")
        .expect("Should have been able to read the file");

    let lines = contents.lines();    
    let mut position = 50;
    let mut counter = 0;

    for line in lines{
        if line.starts_with("L"){
            position -= line[1..].parse::<i32>().unwrap();
        } else if line.starts_with("R"){
            position += line[1..].parse::<i32>().unwrap();
        }
        position %= 100;
        if position == 0 {
            counter += 1;
        }
    }
    println!("{}", counter)
}

