use std::fs;

fn main() {
    let contents = fs::read_to_string("src/bin/day12/data_ex.txt")
        .expect("Should have been able to read the file");

    println!("{}", contents);
}
