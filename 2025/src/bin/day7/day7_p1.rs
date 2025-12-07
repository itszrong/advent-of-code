use std::fs;
use std::collections::HashSet;

fn main() {
    let contents = fs::read_to_string("src/bin/day7/data.txt")
        .expect("Should have been able to read the file");

    let mut split = 0;
    let mut beam_set = HashSet::new();
    for line in contents.lines() {
        for (i, coor) in line.chars().enumerate() {
            if coor == 'S' {
                beam_set.insert(i);
            }
            if coor == '^' && beam_set.contains(&i) {
                split += 1;
                beam_set.remove(&i);
                beam_set.insert(&i-1);
                beam_set.insert(&i+1);
            }
        }
    }

    println!("{}", split);
}
